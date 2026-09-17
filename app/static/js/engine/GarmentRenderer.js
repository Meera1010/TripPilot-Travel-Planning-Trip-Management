/**
 * Garment SVG Path Rasterizer & Canvas 2D Renderer
 */
class GarmentRenderer {
  static renderLayer(ctx, layer) {
    if (!layer.visible) return;

    ctx.save();

    // Set Layer Opacity & Blend Mode
    ctx.globalAlpha = layer.opacity;
    ctx.globalCompositeOperation = layer.blendMode;

    // Apply Transformation Matrix (Translate, Rotate, Scale)
    const bounds = layer.getBounds();
    ctx.translate(bounds.cx, bounds.cy);
    ctx.rotate((layer.rotation * Math.PI) / 180);
    ctx.scale(layer.scaleX, layer.scaleY);
    ctx.translate(-layer.width / 2, -layer.height / 2);

    // Draw Vector Path or Image Pattern
    if (layer.svgPath) {
      const path2d = new Path2D(layer.svgPath);

      // Fill Garment Base Color
      ctx.fillStyle = layer.color;
      ctx.fill(path2d);

      // Stroke Outline
      ctx.strokeStyle = 'rgba(0, 0, 0, 0.4)';
      ctx.lineWidth = 2;
      ctx.stroke(path2d);

      // Render Fabric Texture Pattern Overlay if present
      if (layer.patternType === 'stripes') {
        GarmentRenderer.renderStripesOverlay(ctx, layer, path2d);
      } else if (layer.patternType === 'polka') {
        GarmentRenderer.renderPolkaOverlay(ctx, layer, path2d);
      }
    } else {
      // Fallback shape box
      ctx.fillStyle = layer.color;
      ctx.fillRect(0, 0, layer.width, layer.height);
    }

    ctx.restore();
  }

  static renderStripesOverlay(ctx, layer, path2d) {
    ctx.save();
    ctx.clip(path2d);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
    ctx.lineWidth = 6;
    for (let x = -200; x < layer.width + 200; x += 18) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x + layer.height, layer.height);
      ctx.stroke();
    }
    ctx.restore();
  }

  static renderPolkaOverlay(ctx, layer, path2d) {
    ctx.save();
    ctx.clip(path2d);
    ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
    for (let x = 10; x < layer.width; x += 24) {
      for (let y = 10; y < layer.height; y += 24) {
        ctx.beginPath();
        ctx.arc(x, y, 4, 0, Math.PI * 2);
        ctx.fill();
      }
    }
    ctx.restore();
  }
}
