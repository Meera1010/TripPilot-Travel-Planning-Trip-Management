/**
 * Virtual Outfit Designer Studio Module Controller
 */
let studioEngine = null;
let currentDesignId = null;

document.addEventListener('DOMContentLoaded', async () => {
  const canvasEl = document.getElementById('studio-canvas');
  if (!canvasEl) return;

  studioEngine = new CanvasStudio('studio-canvas');

  // Check URL query parameters for design ID
  const urlParams = new URLSearchParams(window.location.search);
  currentDesignId = urlParams.get('id');

  if (currentDesignId) {
    loadDesign(currentDesignId);
  } else {
    // Initial default saree preset
    loadDefaultPresets('saree');
  }

  setupStudioUIEvents();
});

async function loadDesign(designId) {
  try {
    const res = await API.get(`/designs/${designId}`);
    if (res.success && res.data) {
      document.getElementById('design-title-input').value = res.data.title;
      if (res.data.canvas_data) {
        studioEngine.fromJSON(res.data.canvas_data);
        renderLayerList();
      }
    }
  } catch (err) {
    showToast('Failed to load design', 'error');
  }
}

function loadDefaultPresets(category) {
  const preset = SVG_GARMENTS[category] || SVG_GARMENTS['saree'];
  if (preset) {
    studioEngine.addLayer({
      label: preset.name,
      type: 'garment',
      svgPath: preset.svg_path,
      color: preset.default_colors[0],
      x: 200,
      y: 240,
      width: 400,
      height: 650
    });
    renderLayerList();
  }
}

function setupStudioUIEvents() {
  // Preset buttons
  document.querySelectorAll('.preset-item').forEach(btn => {
    btn.addEventListener('click', () => {
      const cat = btn.dataset.category;
      if (SVG_GARMENTS[cat]) {
        const g = SVG_GARMENTS[cat];
        studioEngine.addLayer({
          label: g.name,
          type: 'garment',
          svgPath: g.svg_path,
          color: g.default_colors[0],
          x: 200,
          y: 240,
          width: 400,
          height: 650
        });
        renderLayerList();
      }
    });
  });

  // Layer selection callback
  studioEngine.onLayerSelected = (layer) => {
    renderLayerList();
    if (layer) {
      const colorInput = document.getElementById('layer-color-picker');
      if (colorInput) colorInput.value = layer.color;
    }
  };

  // Color picker change
  const colorPicker = document.getElementById('layer-color-picker');
  if (colorPicker) {
    colorPicker.addEventListener('input', (e) => {
      const selected = studioEngine.getSelectedLayer();
      if (selected) {
        selected.color = e.target.value;
        studioEngine.render();
      }
    });
  }

  // Save Design button
  const saveBtn = document.getElementById('save-design-btn');
  if (saveBtn) {
    saveBtn.addEventListener('click', async () => {
      const title = document.getElementById('design-title-input').value || 'Untitled Outfit';
      const canvasPayload = studioEngine.toJSON();

      try {
        if (currentDesignId) {
          await API.put(`/designs/${currentDesignId}`, {
            title: title,
            canvas_data: canvasPayload,
            create_snapshot: true
          });
          showToast('Design saved successfully!', 'success');
        } else {
          const res = await API.post('/designs', {
            title: title,
            category: 'saree',
            canvas_data: canvasPayload
          });
          if (res.success && res.data) {
            currentDesignId = res.data.id;
            window.history.pushState({}, '', `/studio?id=${currentDesignId}`);
            showToast('Design created and saved!', 'success');
          }
        }
      } catch (err) {
        showToast('Error saving design', 'error');
      }
    });
  }

  // Tech Pack Export button
  const techPackBtn = document.getElementById('export-techpack-btn');
  if (techPackBtn) {
    techPackBtn.addEventListener('click', () => {
      if (currentDesignId) {
        ExportManager.generateTechPackSpecSheet(currentDesignId);
      } else {
        showToast('Please save the design first to export Tech Pack.', 'warning');
      }
    });
  }
}

function renderLayerList() {
  const container = document.getElementById('studio-layer-list');
  if (!container) return;

  container.innerHTML = studioEngine.layers.map((l, idx) => `
    <div class="layer-item ${idx === studioEngine.selectedLayerIndex ? 'active' : ''}" onclick="selectStudioLayer(${idx})">
      <div style="display:flex;align-items:center;gap:8px;">
        <span style="width:12px;height:12px;border-radius:2px;background:${l.color}"></span>
        <span style="font-size:0.85rem;font-weight:500;">${l.label}</span>
      </div>
      <i class="ph-bold ${l.visible ? 'ph-eye' : 'ph-eye-closed'}" onclick="toggleLayerVisibility(event, ${idx})"></i>
    </div>
  `).join('');
}

function selectStudioLayer(index) {
  studioEngine.selectedLayerIndex = index;
  studioEngine.render();
  renderLayerList();
}

function toggleLayerVisibility(e, index) {
  e.stopPropagation();
  studioEngine.layers[index].visible = !studioEngine.layers[index].visible;
  studioEngine.render();
  renderLayerList();
}
