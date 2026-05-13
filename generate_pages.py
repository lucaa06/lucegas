import os
import csv
import json
import re

# Paths
INPUT_CSV = "05 luce gas.csv"
OUTPUT_DIR = "."
IT_DIR = "guide"
EN_DIR = "en/guide"
DOMAIN = "https://lucegashub.art"

# Ensure directories exist
os.makedirs(os.path.join(OUTPUT_DIR, IT_DIR), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, EN_DIR), exist_ok=True)

def sanitize_filename(name):
    name = str(name).lower()
    name = re.sub(r'[^a-z0-9\s-]', '', name)
    name = re.sub(r'[\s-]+', '-', name)
    return name.strip('-')

def generate_schema(keyword, url, lang="it"):
    desc = f"Approfondimento enciclopedico su {keyword}. Guida completa al mercato luce e gas 2026." if lang == "it" else f"Encyclopedic deep dive on {keyword}. Complete guide to the 2026 energy market."
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": keyword.title(),
        "description": desc,
        "author": {"@type": "Organization", "name": "LUCE/GAS"},
        "publisher": {"@type": "Organization", "name": "LUCE/GAS"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "datePublished": "2026-05-13",
        "dateModified": "2026-05-13"
    }
    return json.dumps(schema)

def get_html_template(keyword, category, intent, page_type, lang="it", slug="", cat_slug=""):
    title = f"{keyword.title()} | Guida Completa Blog LUCE/GAS 2026" if lang == "it" else f"{keyword.title()} | Complete Guide LUCE/GAS Blog"
    description = f"Tutto quello che devi sapere su {keyword}. Scopri come risparmiare sulla bolletta, analizzare il mercato PUN e PSV, ed evitare i costi nascosti." if lang == "it" else f"Everything you need to know about {keyword}. Discover how to save on bills, analyze the market, and avoid hidden costs."
    url = f"{DOMAIN}/{IT_DIR}/{cat_slug}/{slug}.html" if lang == "it" else f"{DOMAIN}/{EN_DIR}/{cat_slug}/{slug}.html"
    schema_json = generate_schema(keyword, url, lang)
    
    root_path = "../../" if lang == "it" else "../../../"

    nav_links_it = f'''
        <a href="{root_path}index.html">Home</a>
        <a href="{root_path}articoli.html">Blog</a>
        <a href="{root_path}chi-siamo.html">Chi Siamo</a>
        <a href="{root_path}contatti.html">Contatti</a>
    '''
    nav_links_en = f'''
        <a href="{root_path}en/index.html">Home</a>
        <a href="{root_path}en/articoli.html">Blog</a>
        <a href="{root_path}en/chi-siamo.html">About</a>
        <a href="{root_path}en/contatti.html">Contact</a>
    '''
    nav_links = nav_links_it if lang == "it" else nav_links_en

    content_it = f"""
        <div class="article-grid">
            <div class="article-content" data-aos="fade-up" data-aos-duration="800">
                <div class="ad-banner">Spazio Pubblicitario Top (es. 728x90 Leaderboard)</div>
                
                <h2 class="font-heading mt-4">1. Introduzione: Perché parlare di {keyword.title()} nel 2026?</h2>
                <p>Il mercato energetico del 2026 si presenta come uno scenario complesso ma ricco di opportunità per i consumatori attenti. Affrontare il tema di <strong>{keyword}</strong> è il primo passo fondamentale per prendere il controllo delle proprie utenze domestiche o aziendali.</p>
                <p>La categoria di riferimento, <em>{category}</em>, rappresenta una voce di costo che incide pesantemente sul bilancio annuale. Con la fine del mercato tutelato e la completa transizione al mercato libero, l'asimmetria informativa tra fornitori e clienti si è ampliata. Capire esattamente cosa significhi questo argomento permette di difendersi dalle micro-spese nascoste nelle fatture.</p>
                
                <h2 class="font-heading mt-4">2. Analisi del Mercato e Fluttuazioni Tariffarie</h2>
                <p>Con un intento di ricerca <strong>{intent}</strong>, l'utente medio cerca chiarezza in un mare di offerte commerciali identiche. L'andamento degli indici all'ingrosso (come il PUN per l'energia elettrica e il PSV per il gas naturale) detta le regole del gioco.</p>
                <p>Cosa comporta tutto questo nella pratica? Significa che la tariffa che hai firmato due anni fa potrebbe oggi risultare completamente fuori mercato. Analizzando attentamente <strong>{keyword}</strong>, emergono tre pattern fondamentali:</p>
                <ul>
                    <li><strong>La volatilità stagionale:</strong> I prezzi tendono a salire durante i picchi di domanda (inverno per il gas, estate per la luce a causa del condizionamento).</li>
                    <li><strong>Le quote fisse di commercializzazione:</strong> Spesso ignorate, queste quote mensili fisse (espresse in euro/mese) possono vanificare un prezzo basso della materia prima.</li>
                    <li><strong>I costi di sbilanciamento:</strong> Costi accessori che variano a seconda del profilo di consumo dell'utente.</li>
                </ul>

                <div class="ad-banner">Spazio Pubblicitario In-Article 1 (es. 300x250 o Content Ad)</div>

                <h2 class="font-heading mt-4">3. I Pro e i Contro delle Offerte Attuali</h2>
                <p>Quando si valuta l'impatto di <strong>{keyword}</strong>, bisogna soppesare i vantaggi e gli svantaggi delle diverse tipologie contrattuali:</p>
                <h3>Tariffe a Prezzo Fisso</h3>
                <p>Garantiscono stabilità e prevedibilità. Ottime per chi non vuole sorprese in bolletta, ma attenzione al momento della sottoscrizione: fissare il prezzo in un momento di mercato alto significa pagare di più per l'intera durata del contratto (spesso 12 o 24 mesi).</p>
                <h3>Tariffe a Prezzo Indicizzato (PUN/PSV)</h3>
                <p>Permettono di cogliere i ribassi del mercato. Richiedono un minimo di attenzione alle notizie economiche. Se il prezzo della materia prima scende, la bolletta si alleggerisce automaticamente.</p>

                <h2 class="font-heading mt-4">4. Le 5 Regole d'Oro per l'Ottimizzazione Pratica</h2>
                <p>Come applicare concretamente queste informazioni per abbattere i costi? Ecco cinque strategie azionabili fin da oggi:</p>
                <ol>
                    <li><strong>Monitoraggio Attivo:</strong> Installa l'app del tuo distributore locale (non del fornitore, ma del distributore, es. E-Distribuzione) per verificare l'effettivo andamento dei tuoi consumi orari e giornalieri.</li>
                    <li><strong>Efficienza degli Elettrodomestici:</strong> Sostituire un vecchio frigorifero o un boiler elettrico con modelli a pompa di calore o ad alta efficienza classe A.</li>
                    <li><strong>Smart Home e Domotica:</strong> Utilizza prese intelligenti programmabili per far funzionare gli elettrodomestici energivori (lavatrice, lavastoviglie) esclusivamente nelle fasce orarie in cui la tua tariffa costa meno (F2/F3).</li>
                    <li><strong>Manutenzione Impianti:</strong> Una caldaia non pulita o dei termosifoni non sfiatati possono aumentare i consumi di gas del 10-15%.</li>
                    <li><strong>Rinegoziazione Annuale:</strong> Non essere fedele al fornitore. Ogni 12 mesi verifica se le tue condizioni contrattuali sono ancora vantaggiose rispetto ai benchmark di mercato.</li>
                </ol>
                
                <div class="ad-banner">Spazio Pubblicitario In-Article 2 (es. Native Ad)</div>

                <h2 class="font-heading mt-4">5. Il Futuro della Transizione Ecologica</h2>
                <p>Il tema di <strong>{keyword}</strong> è intrinsecamente legato agli obiettivi di sostenibilità europea del 2030 e 2050. L'adozione massiccia del fotovoltaico residenziale, le comunità energetiche rinnovabili (CER) e l'elettrificazione del riscaldamento cambieranno per sempre il nostro approccio.</p>
                <p>Essere consapevoli di come gestire questa transizione significa trasformare una spesa passiva in un asset. Molti consumatori stanno già sfruttando gli incentivi per passare all'autoconsumo totale.</p>

                <h2 class="font-heading mt-4">6. Conclusioni Finali</h2>
                <p>Scegliere la migliore soluzione in ambito <strong>{keyword}</strong> è l'unico modo per proteggere il proprio potere d'acquisto dall'inflazione energetica. Rimani aggiornato sulle ultime novità leggendo i nostri approfondimenti periodici e iscriviti per ricevere alert sui cambi di tariffa più convenienti sul mercato.</p>

                <div class="ad-banner">Spazio Pubblicitario Bottom (es. 728x90 Leaderboard)</div>
            </div>
            
            <aside class="sidebar" data-aos="fade-left" data-aos-duration="1000">
                <div class="ad-banner" style="min-height: 600px;">Spazio Pubblicitario Sidebar (es. 300x600 Half Page)</div>
                
                <h3 class="font-heading mt-5 mb-3" style="font-size: 1.2rem;">Articoli Correlati e Top Trend</h3>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 10px;"><a href="{root_path}guide/tariffe-luce/tariffe-luce.html" style="color: var(--accent); text-decoration: none; font-weight: 600;">Le nuove Tariffe Luce 2026: Guida al Risparmio</a></li>
                    <li style="margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 10px;"><a href="{root_path}guide/tariffe-gas/tariffe-gas.html" style="color: var(--accent); text-decoration: none; font-weight: 600;">Andamento PSV: Quando conviene fissare il prezzo del Gas?</a></li>
                    <li style="margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 10px;"><a href="{root_path}guide/consigli-risparmio/ridurre-bolletta-luce.html" style="color: var(--accent); text-decoration: none; font-weight: 600;">5 Trucchi per Dimezzare la Bolletta Elettrica</a></li>
                </ul>
            </aside>
        </div>
    """
    
    content_en = f"""
        <div class="article-grid">
            <div class="article-content" data-aos="fade-up" data-aos-duration="800">
                <div class="ad-banner">Top Ad Space (e.g., 728x90 Leaderboard)</div>
                
                <h2 class="font-heading mt-4">1. Introduction: Why Discuss {keyword.title()} in 2026?</h2>
                <p>The 2026 energy market presents a complex scenario but is rich in opportunities for careful consumers. Addressing the topic of <strong>{keyword}</strong> is the first fundamental step to taking control of your domestic or corporate utilities.</p>
                <p>The reference category, <em>{category}</em>, represents a cost item that heavily impacts the annual budget. With the end of the protected market and the complete transition to the free market, the information asymmetry between suppliers and customers has widened. Understanding exactly what this topic means allows you to defend against micro-expenses hidden in invoices.</p>
                
                <h2 class="font-heading mt-4">2. Market Analysis and Tariff Fluctuations</h2>
                <p>With an intent of <strong>{intent}</strong>, the average user seeks clarity in a sea of identical commercial offers. The trend of wholesale indices (such as PUN for electricity and PSV for natural gas) dictates the rules of the game.</p>
                <p>What does all this mean in practice? It means that the tariff you signed two years ago might now be completely uncompetitive. By carefully analyzing <strong>{keyword}</strong>, three fundamental patterns emerge:</p>
                <ul>
                    <li><strong>Seasonal volatility:</strong> Prices tend to rise during peak demand (winter for gas, summer for electricity due to air conditioning).</li>
                    <li><strong>Fixed marketing fees:</strong> Often ignored, these fixed monthly fees can negate a low raw material price.</li>
                    <li><strong>Imbalance costs:</strong> Additional costs that vary depending on the user's consumption profile.</li>
                </ul>

                <div class="ad-banner">In-Article Ad Space 1 (e.g., 300x250 or Content Ad)</div>

                <h2 class="font-heading mt-4">3. Pros and Cons of Current Offers</h2>
                <p>When evaluating the impact of <strong>{keyword}</strong>, one must weigh the advantages and disadvantages of different contract types:</p>
                <h3>Fixed Price Tariffs</h3>
                <p>They guarantee stability and predictability. Excellent for those who want no surprises on their bill, but be careful when signing: fixing the price in a high market moment means paying more for the entire contract duration (often 12 or 24 months).</p>
                <h3>Indexed Price Tariffs (PUN/PSV)</h3>
                <p>They allow you to catch market downturns. They require a minimum of attention to economic news. If the raw material price drops, the bill automatically lightens.</p>

                <h2 class="font-heading mt-4">4. The 5 Golden Rules for Practical Optimization</h2>
                <p>How to practically apply this information to cut costs? Here are five actionable strategies starting today:</p>
                <ol>
                    <li><strong>Active Monitoring:</strong> Install your local distributor's app to check the actual trend of your hourly and daily consumption.</li>
                    <li><strong>Appliance Efficiency:</strong> Replace an old refrigerator or electric boiler with heat pump or high-efficiency class A models.</li>
                    <li><strong>Smart Home and Automation:</strong> Use programmable smart plugs to run energy-intensive appliances only during the cheapest time slots.</li>
                    <li><strong>System Maintenance:</strong> An uncleaned boiler or unvented radiators can increase gas consumption by 10-15%.</li>
                    <li><strong>Annual Renegotiation:</strong> Don't be loyal to the supplier. Every 12 months, check if your contract conditions are still advantageous compared to market benchmarks.</li>
                </ol>
                
                <div class="ad-banner">In-Article Ad Space 2 (e.g., Native Ad)</div>

                <h2 class="font-heading mt-4">5. The Future of the Ecological Transition</h2>
                <p>The topic of <strong>{keyword}</strong> is intrinsically linked to the European sustainability goals of 2030 and 2050. The massive adoption of residential photovoltaics, renewable energy communities, and heating electrification will forever change our approach.</p>
                <p>Being aware of how to manage this transition means turning a passive expense into an asset.</p>

                <h2 class="font-heading mt-4">6. Final Conclusions</h2>
                <p>Choosing the best solution regarding <strong>{keyword}</strong> is the only way to protect your purchasing power from energy inflation. Stay updated by reading our periodic insights.</p>

                <div class="ad-banner">Bottom Ad Space (e.g., 728x90 Leaderboard)</div>
            </div>
            
            <aside class="sidebar" data-aos="fade-left" data-aos-duration="1000">
                <div class="ad-banner" style="min-height: 600px;">Sidebar Ad Space (e.g., 300x600 Half Page)</div>
                
                <h3 class="font-heading mt-5 mb-3" style="font-size: 1.2rem;">Related Articles & Trends</h3>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 10px;"><a href="{root_path}en/guide/tariffe-luce/tariffe-luce.html" style="color: var(--accent); text-decoration: none; font-weight: 600;">New 2026 Electricity Tariffs: Savings Guide</a></li>
                    <li style="margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 10px;"><a href="{root_path}en/guide/tariffe-gas/tariffe-gas.html" style="color: var(--accent); text-decoration: none; font-weight: 600;">PSV Trends: When to fix the Gas price?</a></li>
                </ul>
            </aside>
        </div>
    """
    content = content_it if lang == "it" else content_en
    lang_code = "it" if lang == "it" else "en"

    template = f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="{description}" />
    <title>{title}</title>
    <link rel="icon" type="image/png" href="{root_path}assets/img/logo-luce-gas.png" />
    <link href="{root_path}assets/css/awwwards.css" rel="stylesheet" />
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <script type="application/ld+json">{schema_json}</script>
</head>
<body>
    <div id="pb"></div>
    <nav class="nav-awwwards">
        <a href="{root_path}index.html" class="logo-awwwards">
            <img src="{root_path}assets/img/logo-luce-gas.png" alt="LUCE GAS Logo">
            LUCE<span>/</span>GAS
        </a>
        <div class="nav-links">
            {nav_links}
        </div>
    </nav>

    <div class="container-aww header-spacing">
        <div class="section-aww pb-0" data-aos="fade-in" data-aos-duration="1000">
            <p class="font-heading" style="color: var(--accent); font-size: 0.9rem; letter-spacing: 1px;">BLOG / {category.upper()}</p>
            <h1 class="huge-text" style="font-size: clamp(2rem, 5vw, 4rem); margin-top: 1rem;">{keyword.title()}</h1>
            <p class="sub-text">Ultimo aggiornamento: Maggio 2026 | Tempo stimato di lettura: 10 min | Scritto dalla Redazione</p>
        </div>
        
        <hr class="hr-awwwards">
        
        {content}
        
    </div>

    <footer class="mt-5">
        <a href="{root_path}index.html" class="logo-awwwards">
            <img src="{root_path}assets/img/logo-luce-gas.png" alt="LUCE GAS Logo">
            LUCE<span>/</span>GAS
        </a>
        <div class="footer-links">
            <a href="{root_path}note-legali.html">Note Legali</a>
            <a href="{root_path}privacy-policy.html">Privacy</a>
            <a href="{root_path}cookie-policy.html">Cookies</a>
        </div>
        <div class="copyright">© 2026 LUCE/GAS Info.</div>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({{ once: true }});
        window.addEventListener('scroll', () => {{
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            document.getElementById('pb').style.width = (winScroll / height) * 100 + "%";
        }});
    </script>
</body>
</html>
"""
    return template

def generate_article_list(pages_dict, lang="it"):
    root_path = "./" if lang == "it" else "../"
    title = "Blog | LUCE/GAS 2026" if lang == "it" else "Blog | LUCE/GAS"
    
    nav_links = f'''
        <a href="{root_path}index.html">Home</a>
        <a href="{root_path}articoli.html" style="color: var(--accent);">Blog</a>
        <a href="{root_path}chi-siamo.html">Chi Siamo</a>
        <a href="{root_path}contatti.html">Contatti</a>
    '''
    
    content = "<div class='article-grid'><div class='article-content'>"
    content += "<div class='ad-banner'>Spazio Pubblicitario Top Header</div>"
    
    for category, links in pages_dict.items():
        cat_title = category.upper().replace('-', ' ')
        content += f"<div class='mt-5' data-aos='fade-up'><h2 class='section-title font-heading'>{cat_title}</h2><div class='list-awwwards'>"
        for keyword, link in links:
            content += f"<a href='{root_path}{link}'><span style='font-family: Inter, sans-serif; font-size: 1.1rem; font-weight: 500;'>{keyword.title()}</span><span class='arrow'>→</span></a>"
        content += "</div></div>"
    
    content += "</div>"
    content += f"""
        <aside class="sidebar" data-aos="fade-left">
            <div class="ad-banner" style="min-height: 600px; position: sticky; top: 100px;">Spazio Pubblicitario Sticky (300x600)</div>
        </aside>
    </div>
    """
        
    template = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <link rel="icon" type="image/png" href="{root_path}assets/img/logo-luce-gas.png" />
    <link href="{root_path}assets/css/awwwards.css" rel="stylesheet" />
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
</head>
<body>
    <nav class="nav-awwwards">
        <a href="{root_path}index.html" class="logo-awwwards">
            <img src="{root_path}assets/img/logo-luce-gas.png" alt="LUCE GAS Logo">
            LUCE<span>/</span>GAS
        </a>
        <div class="nav-links">
            {nav_links}
        </div>
    </nav>

    <div class="container-aww header-spacing">
        <div class="section-aww pb-0" data-aos="fade-in">
            <h1 class="huge-text font-heading">IL BLOG</h1>
            <p class="sub-text">Esplorazione sistematica dell'ecosistema energetico. Trova le guide perfette per tagliare i costi della tua bolletta in oltre 800 articoli approfonditi.</p>
        </div>
        
        <hr class="hr-awwwards">
        
        {content}
        
    </div>

    <footer class="mt-5">
        <a href="{root_path}index.html" class="logo-awwwards">
            <img src="{root_path}assets/img/logo-luce-gas.png" alt="LUCE GAS Logo">
            LUCE<span>/</span>GAS
        </a>
        <div class="footer-links">
            <a href="{root_path}note-legali.html">Note Legali</a>
            <a href="{root_path}privacy-policy.html">Privacy</a>
            <a href="{root_path}cookie-policy.html">Cookies</a>
        </div>
        <div class="copyright">© 2026 LUCE/GAS Info.</div>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({{ once: true }});
    </script>
</body>
</html>
"""
    return template

def main():
    urls = []
    it_pages = {}
    
    with open(INPUT_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            keyword = row.get('parola_chiave', '')
            if not keyword: continue
            category = row.get('categoria', 'generale')
            intent = row.get('intento', 'informazionale')
            page_type = row.get('tipo', 'long-tail')
            
            slug = sanitize_filename(keyword)
            cat_slug = sanitize_filename(category)
            
            it_cat_dir = os.path.join(OUTPUT_DIR, IT_DIR, cat_slug)
            en_cat_dir = os.path.join(OUTPUT_DIR, EN_DIR, cat_slug)
            os.makedirs(it_cat_dir, exist_ok=True)
            os.makedirs(en_cat_dir, exist_ok=True)
            
            it_filepath = os.path.join(it_cat_dir, f"{slug}.html")
            en_filepath = os.path.join(en_cat_dir, f"{slug}.html")
            
            if cat_slug not in it_pages:
                it_pages[cat_slug] = []
            it_pages[cat_slug].append((keyword, f"{IT_DIR}/{cat_slug}/{slug}.html"))
            
            it_html = get_html_template(keyword, category, intent, page_type, "it", slug, cat_slug)
            en_html = get_html_template(keyword, category, intent, page_type, "en", slug, cat_slug)
            
            with open(it_filepath, 'w', encoding='utf-8') as itf:
                itf.write(it_html)
            with open(en_filepath, 'w', encoding='utf-8') as enf:
                enf.write(en_html)
                
            urls.append(f"{DOMAIN}/{IT_DIR}/{cat_slug}/{slug}.html")
            urls.append(f"{DOMAIN}/{EN_DIR}/{cat_slug}/{slug}.html")
            
    with open(os.path.join(OUTPUT_DIR, 'articoli.html'), 'w', encoding='utf-8') as f:
        f.write(generate_article_list(it_pages, "it"))
        
    import datetime
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n'
    
    # Add root pages
    root_pages = [
        ("", "1.0", "daily"),
        ("articoli.html", "0.9", "daily"),
        ("chi-siamo.html", "0.7", "monthly"),
        ("contatti.html", "0.7", "monthly"),
        ("note-legali.html", "0.5", "yearly"),
        ("privacy-policy.html", "0.5", "yearly"),
        ("cookie-policy.html", "0.5", "yearly")
    ]
    for page, priority, freq in root_pages:
        sitemap_content += f"  <url>\\n    <loc>{DOMAIN}/{page}</loc>\\n    <lastmod>{today}</lastmod>\\n    <changefreq>{freq}</changefreq>\\n    <priority>{priority}</priority>\\n  </url>\\n"
        
    for u in urls:
        sitemap_content += f"  <url>\\n    <loc>{u}</loc>\\n    <lastmod>{today}</lastmod>\\n    <changefreq>weekly</changefreq>\\n    <priority>0.8</priority>\\n  </url>\\n"
    sitemap_content += '</urlset>'
    
    with open(os.path.join(OUTPUT_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as sf:
        sf.write(sitemap_content)
        
    print("Generated all deeply extended Light-mode Editorial Blog pages with new domain and favicons.")

if __name__ == "__main__":
    main()
