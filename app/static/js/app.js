/**
 * Main Application Initializer & Global Event Listener Store
 */
document.addEventListener('DOMContentLoaded', () => {
  console.log('StyleForge Virtual Outfit Designer SaaS App Loaded');

  // Mobile sidebar toggle
  const mobileToggle = document.getElementById('mobile-menu-toggle');
  const sidebar = document.querySelector('.sidebar');
  if (mobileToggle && sidebar) {
    mobileToggle.addEventListener('click', () => {
      sidebar.classList.toggle('open');
    });
  }
});
