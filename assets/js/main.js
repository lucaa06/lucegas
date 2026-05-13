document.addEventListener('DOMContentLoaded', () => {
    // Reading progress bar
    const pb = document.getElementById('pb');
    if (pb) {
        window.addEventListener('scroll', () => {
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrolled = (window.scrollY / docHeight) * 100;
            pb.style.width = `${scrolled}%`;
        });
    }

    // Accessibility widget functionality
    const a11yWidget = document.createElement('div');
    a11yWidget.className = 'accessibility-widget';
    a11yWidget.innerHTML = `
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
    `;
    document.body.appendChild(a11yWidget);

    let highContrast = false;
    a11yWidget.addEventListener('click', () => {
        highContrast = !highContrast;
        if (highContrast) {
            document.documentElement.style.setProperty('--bg-color', '#000000');
            document.documentElement.style.setProperty('--text-primary', '#FFFFFF');
            document.documentElement.style.setProperty('--surface-color', '#111111');
            document.documentElement.style.setProperty('--text-secondary', '#CCCCCC');
        } else {
            document.documentElement.style.setProperty('--bg-color', '#0B0F19');
            document.documentElement.style.setProperty('--text-primary', '#FFFFFF');
            document.documentElement.style.setProperty('--surface-color', '#1A2235');
            document.documentElement.style.setProperty('--text-secondary', '#A0ABC0');
        }
    });

    // Cookie consent banner
    if (!localStorage.getItem('cookieConsent')) {
        const cookieBanner = document.createElement('div');
        cookieBanner.style.position = 'fixed';
        cookieBanner.style.bottom = '0';
        cookieBanner.style.left = '0';
        cookieBanner.style.width = '100%';
        cookieBanner.style.backgroundColor = 'var(--surface-color)';
        cookieBanner.style.padding = '1.5rem';
        cookieBanner.style.display = 'flex';
        cookieBanner.style.justifyContent = 'space-between';
        cookieBanner.style.alignItems = 'center';
        cookieBanner.style.zIndex = '9999';
        cookieBanner.style.boxShadow = '0 -4px 10px rgba(0,0,0,0.5)';
        
        cookieBanner.innerHTML = `
            <div style="flex:1">
                <p>Utilizziamo i cookie (incluso AdSense) per migliorare l'esperienza. Accetti l'uso dei cookie?</p>
            </div>
            <div style="display:flex;gap:1rem;margin-left:1rem">
                <button id="acceptCookies" class="btn btn-primary" style="padding:0.5rem 1rem">Accetta</button>
                <button id="rejectCookies" class="btn" style="background:transparent;border:1px solid var(--text-secondary);color:var(--text-primary);padding:0.5rem 1rem">Rifiuta</button>
            </div>
        `;
        document.body.appendChild(cookieBanner);

        document.getElementById('acceptCookies').addEventListener('click', () => {
            localStorage.setItem('cookieConsent', 'accepted');
            cookieBanner.remove();
        });
        document.getElementById('rejectCookies').addEventListener('click', () => {
            localStorage.setItem('cookieConsent', 'rejected');
            cookieBanner.remove();
        });
    }
});
