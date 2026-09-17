/**
 * Interactive Transformation Handle & Bounding Box Controller
 */
class TransformController {
  static renderBoundingBox(ctx, layer) {
    if (!layer || layer.locked) return;

    ctx.save();
    const bounds = layer.getBounds();

    ctx.translate(bounds.cx, bounds.cy);
    ctx.rotate((layer.rotation * Math.PI) / 180);

    const w = layer.width * layer.scaleX;
    const h = layer.height * layer.scaleY;

    // Draw Selection Bounding Box Outline
    ctx.strokeStyle = '#e63946';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.strokeRect(-w / 2, -h / 2, w, h);
    ctx.setLineDash([]);

    // Draw Corner Handles
    const handleSize = 8;
    ctx.fillStyle = '#ffffff';
    ctx.strokeStyle = '#e63946';
    ctx.lineWidth = 2;

    const corners = [
      [-w / 2, -h / 2], // NW
      [w / 2, -h / 2],  // NE
      [w / 2, h / 2],   // SE
      [-w / 2, h / 2]   // SW
    ];

    corners.forEach(([hx, hy]) => {
      ctx.beginPath();
      ctx.rect(hx - handleSize / 2, hy - handleSize / 2, handleSize, handleSize);
      ctx.fill();
      ctx.stroke();
    });

    // Rotation Handle Top Line
    ctx.beginPath();
    ctx.moveTo(0, -h / 2);
    ctx.lineTo(0, -h / 2 - 24);
    ctx.stroke();

    // Rotation Handle Circle Knob
    ctx.beginPath();
    ctx.arc(0, -h / 2 - 24, 6, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    ctx.restore();
  }
}
