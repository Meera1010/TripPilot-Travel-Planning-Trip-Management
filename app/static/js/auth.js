document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('form-login');
    const registerForm = document.getElementById('form-register');
    const logoutBtn = document.getElementById('btn-logout');

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = document.getElementById('login-username').value;
            const password = document.getElementById('login-password').value;

            try {
                const res = await API.post('/api/auth/login', { username, password });
                window.location.href = '/dashboard';
            } catch (err) {
                alert(err.message || 'Login failed');
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const full_name = document.getElementById('reg-fullname').value;
            const username = document.getElementById('reg-username').value;
            const email = document.getElementById('reg-email').value;
            const password = document.getElementById('reg-password').value;

            try {
                await API.post('/api/auth/register', { full_name, username, email, password });
                alert('Registration successful! Please sign in.');
                window.location.href = '/login';
            } catch (err) {
                alert(err.message || 'Registration failed');
            }
        });
    }

    if (logoutBtn) {
        logoutBtn.addEventListener('click', async () => {
            await API.post('/api/auth/logout');
            window.location.href = '/login';
        });
    }
});
