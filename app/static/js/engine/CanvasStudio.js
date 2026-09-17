/**
 * StyleForge CanvasStudio Core Engine Controller
 */
class CanvasStudio {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;

    this.ctx = this.canvas.getContext('2d');
    this.layers = [];
    this.selectedLayerIndex = -1;

    // Viewport & Grid State
    this.zoomLevel = 1.0;
    this.gridVisible = true;
    this.gridSize = 20;
    this.croquisVisible = true;

    // Interaction State
    this.isDragging = false;
    this.dragStartX = 0;
    this.dragStartY = 0;

    // Undo/Redo Manager
    this.undoManager = new UndoManager();

    this.initEvents();
    this.render();
  }

  initEvents() {
    this.canvas.addEventListener('mousedown', (e) => this.onMouseDown(e));
    this.canvas.addEventListener('mousemove', (e) => this.onMouseMove(e));
    this.canvas.addEventListener('mouseup', () => this.onMouseUp());
  }

  getCanvasCoordinates(e) {
    const rect = this.canvas.getBoundingClientRect();
    const scaleX = this.canvas.width / rect.width;
    const scaleY = this.canvas.height / rect.height;

    return {
      x: (e.clientX - rect.left) * scaleX,
      y: (e.clientY - rect.top) * scaleY
    };
  }

  onMouseDown(e) {
    const coords = this.getCanvasCoordinates(e);

    // Hit test layers from top to bottom
    let hitIndex = -1;
    for (let i = this.layers.length - 1; i >= 0; i--) {
      if (this.layers[i].containsPoint(coords.x, coords.y)) {
        hitIndex = i;
        break;
      }
    }

    if (hitIndex !== -1) {
      this.selectedLayerIndex = hitIndex;
      this.isDragging = true;
      this.dragStartX = coords.x - this.layers[hitIndex].x;
      this.dragStartY = coords.y - this.layers[hitIndex].y;
    } else {
      this.selectedLayerIndex = -1;
    }

    this.render();
    if (typeof this.onLayerSelected === 'function') {
      this.onLayerSelected(this.getSelectedLayer());
    }
  }

  onMouseMove(e) {
    if (!this.isDragging || this.selectedLayerIndex === -1) return;

    const layer = this.layers[this.selectedLayerIndex];
    if (layer.locked) return;

    const coords = this.getCanvasCoordinates(e);
    layer.x = coords.x - this.dragStartX;
    layer.y = coords.y - this.dragStartY;

    this.render();
  }

  onMouseUp() {
    if (this.isDragging) {
      this.isDragging = false;
      this.saveUndoState();
    }
  }

  addLayer(layerConfig) {
    const layer = new Layer(layerConfig);
    this.layers.push(layer);
    this.selectedLayerIndex = this.layers.length - 1;
    this.saveUndoState();
    this.render();
    return layer;
  }

  removeSelectedLayer() {
    if (this.selectedLayerIndex >= 0 && this.selectedLayerIndex < this.layers.length) {
      this.layers.splice(this.selectedLayerIndex, 1);
      this.selectedLayerIndex = -1;
      this.saveUndoState();
      this.render();
    }
  }

  moveLayerUp() {
    if (this.selectedLayerIndex < this.layers.length - 1) {
      const temp = this.layers[this.selectedLayerIndex];
      this.layers[this.selectedLayerIndex] = this.layers[this.selectedLayerIndex + 1];
      this.layers[this.selectedLayerIndex + 1] = temp;
      this.selectedLayerIndex++;
      this.render();
    }
  }

  moveLayerDown() {
    if (this.selectedLayerIndex > 0) {
      const temp = this.layers[this.selectedLayerIndex];
      this.layers[this.selectedLayerIndex] = this.layers[this.selectedLayerIndex - 1];
      this.layers[this.selectedLayerIndex - 1] = temp;
      this.selectedLayerIndex--;
      this.render();
    }
  }

  getSelectedLayer() {
    return this.selectedLayerIndex >= 0 ? this.layers[this.selectedLayerIndex] : null;
  }

  saveUndoState() {
    this.undoManager.saveState(this.toJSON());
  }

  undo() {
    const state = this.undoManager.undo(this.toJSON());
    if (state) this.fromJSON(state);
  }

  redo() {
    const state = this.undoManager.redo(this.toJSON());
    if (state) this.fromJSON(state);
  }

  render() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // 1. Draw Grid Background if enabled
    if (this.gridVisible) {
      this.renderGrid();
    }

    // 2. Draw Croquis Mannequin Silhouette
    if (this.croquisVisible) {
      this.renderCroquis();
    }

    // 3. Render Layers Bottom to Top
    this.layers.forEach((layer) => {
      GarmentRenderer.renderLayer(this.ctx, layer);
    });

    // 4. Render Bounding Box & Transformation Handles for Selected Layer
    const selectedLayer = this.getSelectedLayer();
    if (selectedLayer) {
      TransformController.renderBoundingBox(this.ctx, selectedLayer);
    }
  }

  renderGrid() {
    this.ctx.save();
    this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    this.ctx.lineWidth = 1;

    for (let x = 0; x < this.canvas.width; x += this.gridSize) {
      this.ctx.beginPath();
      this.ctx.moveTo(x, 0);
      this.ctx.lineTo(x, this.canvas.height);
      this.ctx.stroke();
    }
    for (let y = 0; y < this.canvas.height; y += this.gridSize) {
      this.ctx.beginPath();
      this.ctx.moveTo(0, y);
      this.ctx.lineTo(this.canvas.width, y);
      this.ctx.stroke();
    }
    this.ctx.restore();
  }

  renderCroquis() {
    this.ctx.save();
    this.ctx.globalAlpha = 0.35;
    this.ctx.strokeStyle = '#8d99ae';
    this.ctx.lineWidth = 2;

    // Standard Fashion Model Croquis Outline Path
    const cx = 400;
    this.ctx.beginPath();
    // Head
    this.ctx.ellipse(cx, 160, 20, 28, 0, 0, Math.PI * 2);
    // Neck & Shoulders
    this.ctx.moveTo(cx - 10, 188);
    this.ctx.lineTo(cx - 10, 210);
    this.ctx.lineTo(cx - 65, 235); // Left shoulder
    this.ctx.moveTo(cx + 10, 188);
    this.ctx.lineTo(cx + 10, 210);
    this.ctx.lineTo(cx + 65, 235); // Right shoulder
    // Torso & Waist
    this.ctx.lineTo(cx + 45, 340); // Bust to Waist
    this.ctx.lineTo(cx + 60, 420); // Waist to Hips
    this.ctx.lineTo(cx + 35, 680); // Legs
    this.ctx.lineTo(cx + 30, 920); // Ankle
    this.ctx.stroke();

    this.ctx.beginPath();
    this.ctx.moveTo(cx - 65, 235);
    this.ctx.lineTo(cx - 45, 340);
    this.ctx.lineTo(cx - 60, 420);
    this.ctx.lineTo(cx - 35, 680);
    this.ctx.lineTo(cx - 30, 920);
    this.ctx.stroke();

    this.ctx.restore();
  }

  toJSON() {
    return {
      dimensions: { width: this.canvas.width, height: this.canvas.height },
      layers: this.layers.map(l => l.toJSON())
    };
  }

  fromJSON(json) {
    if (!json || !json.layers) return;
    this.layers = json.layers.map(lConfig => new Layer(lConfig));
    this.selectedLayerIndex = this.layers.length > 0 ? 0 : -1;
    this.render();
  }
}
