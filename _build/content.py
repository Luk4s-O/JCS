# Every list on the site, in one place.
#
# To add something: add a line below, then run   python3 _build/build.py   from the repo root.
# That rewrites the list pages, the blog cards and the homepage search index as plain HTML.
# Lists sort themselves alphabetically; runways sort themselves by year, season, then brand.
#
# href: a full https:// link, or a path from the site root (e.g. "blog/fashion/runways.html").
# A page that should have its own generated list page gets  "page": True  and  "items": [...].
# "search": extra words that find an item in the homepage search without being shown.
# GitHub Pages does not publish this _build folder.

SITE = [
    {"title": "Blog", "href": "blog.html", "page": "cards", "items": [
        {"title": "Activism", "href": "blog/activism.html", "page": True, "items": []},
        {"title": "Architecture & Urbanism", "href": "blog/architecture-urbanism.html", "page": True, "items": []},
        {"title": "Cinematography", "href": "blog/cinematography.html", "page": True, "items": []},
        {"title": "Design", "href": "blog/design.html", "page": True, "items": []},
        {"title": "Fashion", "href": "blog/fashion.html", "page": True, "items": [
            {"title": "Local Designers", "href": "blog/fashion/local-designers.html", "page": True, "items": []},
            {"title": "Local Jewelers", "href": "blog/fashion/local-jewelers.html", "page": True, "items": []},
            {"title": "Runways", "href": "blog/fashion/runways.html", "page": True,
             "note": '<a href="https://www.youtube.com/playlist?list=PLONN2I1j-pYs">YouTube playlist</a>',
             "runways": [
                # Shown as "Brand - Year - Season", plus "(line)" when a brand had several shows that season.
                {"brand": "Enfants Riches Déprimés", "year": 2026, "season": "Fall/Winter", "href": "https://www.youtube.com/watch?v=7d7Yj2HtayA"},
                {"brand": "Prada", "year": 2026, "season": "Fall/Winter", "line": "Menswear", "href": "https://www.youtube.com/watch?v=J1GCDcbYIRI"},
                {"brand": "Prada", "year": 2026, "season": "Fall/Winter", "line": "Womenswear", "href": "https://www.youtube.com/watch?v=bX8UfV0MqTw"},
                {"brand": "Vivienne Westwood", "year": 1993, "season": "Fall/Winter", "href": "https://www.youtube.com/watch?v=Pfhvm-9yVFU"},
             ]},
        ]},
        {"title": "Music", "href": "blog/music.html", "page": True, "items": []},
        {"title": "Nutrition", "href": "blog/nutrition.html", "page": True, "items": []},
        {"title": "Philosophy", "href": "blog/philosophy.html", "page": True, "items": []},
        {"title": "Politics", "href": "blog/politics.html", "page": True, "items": []},
        {"title": "Science & Technology", "href": "blog/science-technology.html", "page": True, "items": []},
        {"title": "Telegram Channels", "href": "blog/telegram-channels.html", "page": True, "items": [
            # Names as the channels call themselves (emoji and fancy lettering removed); "search" adds the @handle to search.
            {"title": "GruppaOF Official", "href": "https://t.me/Gruppa_OF", "search": "@Gruppa_OF"},
            {"title": "Hooligans.cz", "href": "https://t.me/hooliganscz1999", "search": "@hooliganscz1999"},
            {"title": "POPULAR FRONT", "href": "https://t.me/POPULARXFRONT", "search": "@POPULARXFRONT"},
            {"title": "frontier_conflict", "href": "https://t.me/frontier_conflict1", "search": "@frontier_conflict1"},
            {"title": "ProjectLeaflet", "href": "https://t.me/TheLeaflet", "search": "@TheLeaflet"},
            {"title": "Our Wars, Today", "href": "https://t.me/ourwarstoday", "search": "@ourwarstoday"},
            {"title": "Primal Diets | Carnivore, Aajonus, Keto, Weston Price, etc.", "href": "https://t.me/primaldiets", "search": "@primaldiets"},
            {"title": "why we still here? just to suffer?", "href": "https://t.me/whywestillherejustto", "search": "@whywestillherejustto"},
            {"title": "Primal Literature", "href": "https://t.me/primalstudy", "search": "@primalstudy"},
            {"title": "Sebastian's Channel", "href": "https://t.me/c/3776455781/3"},  # private channel
            {"title": "radiohorses", "href": "https://t.me/radiohead_horses", "search": "@radiohead_horses"},
            {"title": "The Space Techie", "href": "https://t.me/spacetechie", "search": "@spacetechie"},
            {"title": "The Black Lodge", "href": "https://t.me/tasogaredoki", "search": "@tasogaredoki"},
            {"title": "TheTomboysOrganization", "href": "https://t.me/tomboysExist11", "search": "@tomboysExist11"},
            {"title": "FPVS SOCIAL FIGHT CLUB", "href": "https://t.me/fpvsfight", "search": "@fpvsfight"},
            {"title": "Aajonus Vonderplanitz Archive", "href": "https://t.me/AajonusVonderplanitzArchive", "search": "@AajonusVonderplanitzArchive"},
            {"title": "Raw Primal Diet / Primal Healing", "href": "https://t.me/linaascending", "search": "@linaascending"},
            {"title": "Weston A. Price Foundation", "href": "https://t.me/westonaprice", "search": "@westonaprice"},
            {"title": "фунгобомбер", "href": "https://t.me/fungobomber", "search": "@fungobomber"},
            {"title": "AWAY DAYS", "href": "https://t.me/awaydaystv", "search": "@awaydaystv"},
            {"title": "Ditto Nation", "href": "https://t.me/ditto_nation", "search": "@ditto_nation"},
            {"title": "Ditto National Library", "href": "https://t.me/ditto_national_library", "search": "@ditto_national_library"},
            {"title": "The Primal Diet by Aajonus Vonderplanitz", "href": "https://t.me/primal_diet", "search": "@primal_diet"},
            {"title": "Dis-moi ce que tu manges, je te dirai ce que tu es", "href": "https://t.me/HealthThruNutrition", "search": "@HealthThruNutrition"},
            {"title": "Primal Kitchen", "href": "https://t.me/eatmorefat", "search": "@eatmorefat"},
            {"title": "b///ardak", "href": "https://t.me/bbbardak", "search": "@bbbardak"},
        ]},
        {"title": "Videogames", "href": "blog/videogames.html", "page": True, "items": []},
    ]},
    {"title": "Coffee", "href": "coffee.html", "page": True, "items": [
        {"title": "Notes on cheap high quality brewing water preparation", "href": "coffeeWater.html", "crumb": "water mineralisation"},
        {"title": "SCA's flavor wheel", "href": "flavorWheel.html", "crumb": "sca flavor wheel"},
    ]},
    {"title": "Essays", "heading": "A collection of interesting essays", "tab": "Essays library", "href": "essays.html", "page": True, "items": [
        {"title": "Geeks, MOPs, and sociopaths in subculture evolution", "href": "https://meaningness.com/geeks-mops-sociopaths"},
    ]},
    {"title": "Fun stuff", "href": "fun-stuff.html", "page": True, "items": [
        {"title": "Cool ASCII animation tool", "href": "animation.html", "crumb": "ascii animation tool"},
    ]},
    {"title": "Projects", "href": "projects.html", "page": True, "items": [
        {"title": "Kitten Leg Prosthetic", "href": "projects/kitten-leg-prosthetic.html", "page": True, "items": []},
        {"title": "Oblecko - Wardrobe management app", "href": "https://oblecko.zatisie.workers.dev"},
        {"title": "Oblecko - Wardrobe management app demo (password: demo)", "href": "oblecko-demo.html"},
    ]},
]

# Season order within a year, for runways. Unknown seasons go last.
SEASONS = ["Resort", "Spring/Summer", "Pre-Fall", "Fall/Winter"]
