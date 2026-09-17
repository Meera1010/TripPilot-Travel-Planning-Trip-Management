/**
 * Digital Fashion Sketchbook Studio Module Controller
 */
document.addEventListener('DOMContentLoaded', () => {
  const sketchCanvas = document.getElementById('sketchbook-canvas');
  if (!sketchCanvas) return;

  const ctx = sketchCanvas.getContext('2d');
  let isDrawing = false;
  let currentStrokeColor = '#000000';
  let strokeWidth = 3;

  function renderCroquisBackground() {
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, sketchCanvas.width, sketchCanvas.height);

    ctx.save();
    ctx.strokeStyle = '#e0e0e0';
    ctx.lineWidth = 1;
    ctx.globalAlpha = 0.4;

    const cx = sketchCanvas.width / 2;
    ctx.beginPath();
    ctx.ellipse(cx, 140, 20, 26, 0, 0, Math.PI * 2);
    ctx.moveTo(cx - 50, 200); ctx.lineTo(cx + 50, 200);
    ctx.moveTo(cx - 35, 300); ctx.lineTo(cx + 35, 300);
    ctx.moveTo(cx - 45, 400); ctx.lineTo(cx + 45, 400);
    ctx.moveTo(cx - 25, 750); ctx.lineTo(cx + 25, 750);
    ctx.stroke();
    ctx.restore();
  }

  renderCroquisBackground();

  sketchCanvas.addEventListener('mousedown', (e) => {
    isDrawing = true;
    const rect = sketchCanvas.getBoundingClientRect();
    ctx.beginPath();
    ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
  });

  sketchCanvas.addEventListener('mousemove', (e) => {
    if (!isDrawing) return;
    const rect = sketchCanvas.getBoundingClientRect();
    ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
    ctx.strokeStyle = currentStrokeColor;
    ctx.lineWidth = strokeWidth;
    ctx.lineCap = 'round';
    ctx.stroke();
  });

  sketchCanvas.addEventListener('mouseup', () => isDrawing = false);

  const clearBtn = document.getElementById('clear-sketch-btn');
  if (clearBtn) {
    clearBtn.addEventListener('click', () => renderCroquisBackground());
  }
});
