/**
 * Technical Spec & Measurement Profiles Module Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const container = document.getElementById('sizing-wrapper');
  if (!container) return;

  loadProfiles();
});

async function loadProfiles() {
  const tableBody = document.getElementById('profiles-tbody');
  if (!tableBody) return;

  try {
    const res = await API.get('/sizing/profiles');
    if (res.success && res.data) {
      tableBody.innerHTML = res.data.map(p => `
        <tr>
          <td><strong>${p.name}</strong></td>
          <td>${p.gender.toUpperCase()}</td>
          <td>${p.bust_chest}"</td>
          <td>${p.waist}"</td>
          <td>${p.hips}"</td>
          <td>${p.height}"</td>
          <td><span class="badge ${p.is_standard_size ? 'badge-approved' : 'badge-review'}">${p.standard_size_code}</span></td>
        </tr>
      `).join('');
    }
  } catch (err) {
    console.error('Error loading profiles:', err);
  }
}
