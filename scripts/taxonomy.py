# Theme taxonomy and cleaning for the Data Practice Atlas (pass of 20 Nov 2026).
# Every theme maps to exactly one family. Each entry gets an explicit `family` (drives colour, shape, pattern)
# and `tag_families` (one family per theme, same order as `tags`).

# 1. Synonyms / spelling merges (old -> new). None = drop the theme.
MERGE = {
    "data-journalism": "journalism", "dataviz": "information-design", "infographics": "information-design",
    "method": "methods", "survey": "surveys", "education": "teaching", "courses": "teaching", "tutorials": "teaching",
    "how-to": "teaching", "ggplot2": "r", "charts": "information-design", "tool": None, "tools": None,
    "web-dataviz": "information-design", "graphics": "information-design", "data-design": "information-design",
    "maps": "maps", "mapping_theme": "maps", "visualising-data-catalogue": None,
}

# 2. Family of every theme.
FAMILY = {}
def put(fam, words):
    for w in words.split():
        assert w not in FAMILY, w
        FAMILY[w] = fam

put("design", """information-design art data-art storytelling data-humanism process design creative-coding music craft sound
 physicalisation creative-tech generative drawing diagrams illustration pictograms product dashboards speculative-design motion
 showcase data-experience data-products comics interaction-design critical-design architecture sonification personal-data narrative
 hierarchy workbook practice installation branding photography timelines thinking print business""")
put("rights", """ai-ethics human-rights activism race power ethics surveillance data-feminism algorithms digital-rights gender data-gaps
 data-justice privacy facial-recognition bias evidence design-justice migration inequality welfare internet-health hacking
 data-colonialism civilian-harm military arms conflict fairness extraction gdpr justice law technochauvinism inclusion
 accessibility data-politics""")
put("civic", """cities open-data official-statistics civic-data civic-tech policy government development participatory democracy society
 data-governance tourism decision-intelligence politics humanitarian demography legibility regional crisis census smart-city
 civic-systems open-government public-spending agriculture housing surveys transparency transport citizenship infrastructure
 overtourism data-collaboratives labour companies gtfs complaints sensing""")
put("journalism", """journalism investigation fact-checking misinformation osint media-startups media corruption""")
put("research", """research teaching statistics history economics complexity theory classic networks ml ai critique science academic
 trade humanities data-science nlp public-health hci classification forecasting information-theory digital-humanities
 cultural-analytics health literacy methods open-access finance open-science controversy-mapping information media-history
 digital-methods indices public-speaking""")
put("maps", """maps spatial-analysis trees animals tracking space nature cartography aviation counter-mapping biodiversity earth oceans
 birds weather climate energy emissions forests earth-observation real-time boundaries citizen-science""")
put("regions", """italy latin-america africa asia india mena europe nordic""")
put("culture", """weird community archive food film public-domain internet events web digital-society search citizen-reports
 crowdsourced games books multidisciplinary toys open-knowledge news museums technology humour culture talks sport awards
 documentary interviews podcast digital-culture attention tv email names crowdfunding words""")
put("tools", """coding specialist charting data complex colour mapping open-source d3 r python reference datasets knowledge-graph""")

TOOL_SECTIONS = ["charting","coding","complex","mapping","data","colour","specialist"]

def clean(recs):
    unknown = set()
    for r in recs:
        src = []
        tags = []
        for t in r["tags"]:
            t = t.strip().lower()
            if t == "visualising-data-catalogue":
                src.append("Visualising Data catalogue"); continue
            # "mapping" is a tool section; on non-tools it means the maps theme
            if t == "mapping" and r["category"] != "Tool": t = "maps"
            if t in MERGE: t = MERGE[t]
            if not t or t in tags: continue
            tags.append(t)
        # tools: section first
        if r["category"] == "Tool":
            sec = [t for t in tags if t in TOOL_SECTIONS]
            tags = sec + [t for t in tags if t not in TOOL_SECTIONS]
        for t in tags:
            if t not in FAMILY: unknown.add(t)
        r["tags"] = tags
        r["tag_families"] = [FAMILY.get(t, "culture") for t in tags]
        r["source"] = "; ".join(src)
        # explicit family rule
        if r["category"] == "Tool":
            fam = "tools"
        else:
            score = {}
            for i, (t, f) in enumerate(zip(tags, r["tag_families"])):
                if f in ("regions", "tools"): continue
                score[f] = score.get(f, 0) + (1.5 if i == 0 else 1.0) - i * 0.01
            if score:
                fam = max(score, key=score.get)
            elif any(f == "tools" for f in r["tag_families"]):
                fam = "tools"
            elif any(f == "regions" for f in r["tag_families"]):
                fam = "regions"
            else:
                fam = "culture"
        r["family"] = fam
    assert not unknown, sorted(unknown)
    return recs
