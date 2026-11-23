# Merges Andy Kirk's Visualising Data resources catalogue (read 19 Nov 2026) into the Atlas as category "Tool".
SECTION_NOTE = {
 "CHARTING":"Tool for making charts and exploring data, mostly no-code or low-code.",
 "CODING":"Library, framework or environment for building charts and visualisations in code.",
 "COMPLEX":"Tool for multivariate, network, flow or text/qualitative visualisation.",
 "MAPPING":"Mapping or spatial-analysis package, utility or library.",
 "DATA":"Tool for collecting, extracting, cleaning or transforming data.",
 "COLOUR":"Tool or guide for building and checking colour palettes.",
 "SPECIALIST":"Design, presentation, publishing or niche workflow tool.",
}
# Known (Claude's knowledge, check) to be discontinued or frozen. Andy's page itself warns some entries are obsolete.
ARCHIVED = {"Mapzen","Polymaps","Modest-Maps","Daytum","Quadrigram","Tagxedo","Scriptographer","Streamtools","Dotspotting",
 "Kartograph","Odyssey.js","Chartbuilder","Dimple","Polychart.js","rCharts","Envision","Cubism.js","Lovely-Charts","Arbor.js",
 "Stamen-Maps","DataPad","ScraperWiki","Vischeck","TimeFlow"}
# Atlas entries that already exist: (atlas name) -> catalogue name
EXISTING = {"RAWGraphs":"RAWGraphs","D3.js":"D3.js","ai2html":"ai2html","ColorBrewer":"ColorBrewer","Viz Palette":"Viz Palette",
 "Gephi":"Gephi","QGIS":"QGIS","Datawrapper":"Datawrapper","Flourish":"Flourish","Natural Earth":"Natural-Earth"}
MOVE_TO_TOOL = {"RAWGraphs":"CHARTING","D3.js":"CODING","ai2html":"CODING","ColorBrewer":"COLOUR","Viz Palette":"COLOUR",
 "Gephi":"COMPLEX","QGIS":"MAPPING","kepler.gl":"MAPPING"}
V="verified this session"

def merge(recs):
    sec=None; cat=[]
    for line in open("vd_catalogue.txt"):
        line=line.strip()
        if not line: continue
        if "|" not in line: sec=line; continue
        n,u=line.split("|",1); fixed=u.endswith("*"); u=u.rstrip("*")
        cat.append((sec,n,u,fixed))
    assert len(cat)==293, len(cat)
    by_name={r["name"]:r for r in recs}
    covered={EXISTING[a] for a in MOVE_TO_TOOL if a in EXISTING}
    SUFFIX={"Datawrapper","Flourish","Natural-Earth"}
    tag="visualising-data-catalogue"
    for an,cn in EXISTING.items():
        r=by_name[an]; r["tags"]=r["tags"]+[tag]
    for an,s in MOVE_TO_TOOL.items():
        r=by_name[an]; r["category"]="Tool"; r["tags"]=[t for t in r["tags"] if t!="tool"]+[s.lower()]
        r["who"]=("Visualising Data · "+s.title()) if an in EXISTING else "Added by Claude · not in the catalogue"
    for sec,n,u,fixed in cat:
        if n in covered: continue
        disp=n if n in {"think-cell","IN-SPIRE","DIVA-GIS"} else n.replace("-"," ")
        if n in SUFFIX: disp+=" (tool)"
        for a,b in [("Microsoft PowerPoint","Microsoft PowerPoint"),("HTML Widgets for R","htmlwidgets for R"),("e!Sankey","e!Sankey")]:
            disp=disp.replace(a,b)
        note=""
        recs.append({"name":disp,"category":"Tool","who":"Visualising Data · "+sec.title(),"year":"","place":"","tags":[sec.lower(),tag],
            "note":note,"url":u,"seed":False,"status":"active","verified":V})
    return recs
