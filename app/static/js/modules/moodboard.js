/**
 * Moodboard Visual Canvas & Color Harmony Module Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const container = document.getElementById('moodboard-container');
  if (!container) return;

  loadMoodboards();

  const harmonyBtn = document.getElementById('btn-generate-harmony');
  if (harmonyBtn) {
    harmonyBtn.addEventListener('click', async () => {
      const baseHex = document.getElementById('harmony-base-color').value || '#d90429';
      const harmonyType = document.getElementById('harmony-type-select').value || 'analogous';

      try {
        const res = await API.post('/moodboards/color-harmony', { base_hex: baseHex, harmony_type: harmonyType });
        if (res.success && res.data) {
          renderHarmonyPalette(res.data);
        }
      } catch (err) {
        showToast('Error generating color harmony', 'error');
      }
    });
  }
});

async function loadMoodboards() {
  const container = document.getElementById('moodboard-container');
  try {
    const res = await API.get('/moodboards');
    if (res.success && res.data) {
      container.innerHTML = res.data.map(m => `
        <div class="card moodboard-card">
          <div class="moodboard-preview-canvas">
            <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:8px;width:80%;height:80%;">
              ${(m.palettes[0]?.hex_codes || ['#d90429', '#e9c46a', '#1d3557']).map(hex => `
                <div style="background:${hex};border-radius:4px;"></div>
              `).join('')}
            </div>
          </div>
          <div style="padding:16px;">
            <h4 style="font-size:1rem;font-weight:600;margin-bottom:4px;">${m.title}</h4>
            <p style="font-size:0.8rem;color:var(--text-secondary);">${m.description || 'No description'}</p>
          </div>
        </div>
      `).join('');
    }
  } catch (err) {
    console.error('Error loading moodboards:', err);
  }
}

function renderHarmonyPalette(data) {
  const container = document.getElementById('harmony-result-swatches');
  if (!container) return;

  container.innerHTML = data.hex_codes.map((hex, idx) => `
    <div style="flex:1;text-align:center;">
      <div style="height:60px;background:${hex};border-radius:var(--radius-md);margin-bottom:6px;"></div>
      <span style="font-size:0.75rem;font-weight:600;display:block;">${hex}</span>
      <span style="font-size:0.65rem;color:var(--text-muted);display:block;">${data.pantone_codes[idx] || ''}</span>
    </div>
  `).join('');
}
