// Consent Mode v2 helper — called on accept to signal Google
function _grantConsent() {
    if (typeof gtag === 'function') {
        gtag('consent', 'update', {
            'ad_storage': 'granted',
            'analytics_storage': 'granted',
            'ad_user_data': 'granted',
            'ad_personalization': 'granted'
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Reading progress bar
    const pb = document.getElementById('pb');
    if (pb) {
        const onScroll = () => {
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            if (docHeight > 0) pb.style.width = `${(window.scrollY / docHeight) * 100}%`;
        };
        window.addEventListener('scroll', onScroll, { passive: true });
    }

    // GDPR Cookie consent
    if (!localStorage.getItem('cookieConsent')) {
        const banner = document.createElement('div');
        banner.className = 'cookie-banner';
        banner.innerHTML = `
            <p>Utilizziamo cookie tecnici e, previo consenso, cookie di profilazione (es. Google AdSense) per mostrare annunci pertinenti. <a href="/cookie-policy.html" style="color:#fff;text-decoration:underline;">Cookie Policy</a></p>
            <div class="cookie-banner-actions">
                <button class="cookie-btn-accept" id="cookieAccept">Accetta</button>
                <button class="cookie-btn-reject" id="cookieReject">Rifiuta</button>
            </div>
        `;
        document.body.appendChild(banner);

        document.getElementById('cookieAccept').addEventListener('click', () => {
            localStorage.setItem('cookieConsent','accepted');
            localStorage.setItem('ck_ts', new Date().toISOString());
            _grantConsent();
            banner.remove();
        });
        document.getElementById('cookieReject').addEventListener('click', () => {
            localStorage.setItem('cookieConsent','rejected');
            localStorage.setItem('ck_ts', new Date().toISOString());
            banner.remove();
        });
    }
});
