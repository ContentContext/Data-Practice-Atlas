# Builds the curated data atlas: data.json + data.csv
# Fields: name | category | who | year | place | tags | note | url | seed | status | verified
import json, csv

V = "verified this session"
K = "from Claude's knowledge; check link"

rows = [
# ---------- BOOKS ----------
("Dear Data","Book","Giorgia Lupi & Stefanie Posavec","2016","New York / London","data-humanism;drawing;personal-data","A year of weekly hand-drawn postcards, each logging one small slice of daily life. The founding text of slow, personal data drawing.","https://www.dear-data.com",1,"active",K),
("Data Feminism","Book","Catherine D'Ignazio & Lauren F. Klein","2020","MIT Press","data-feminism;power;ethics","Seven principles for examining who collects data, who benefits and who is left out. Open-access edition online.","https://data-feminism.mitpress.mit.edu",1,"active",K),
("Factfulness","Book","Hans Rosling, Ola Rosling, Anna Rosling Rönnlund","2018","Sceptre / Flatiron","statistics;development;bias","Ten instincts that distort how we read the world, and how to check them against data.","https://www.gapminder.org/factfulness-book/",1,"active",K),
("Why Information Grows","Book","César Hidalgo","2015","Basic Books","complexity;economics;information","Economies as systems that accumulate knowledge and know-how; the theory behind economic complexity.","https://en.wikipedia.org/wiki/Why_Information_Grows",1,"active",K),
("Visual Complexity: Mapping Patterns of Information","Book","Manuel Lima","2011","Princeton Architectural Press","networks;complexity;history","A survey of network visualisation, from medieval diagrams to contemporary graphs.","https://www.visualcomplexity.com/vc/book/",1,"active",K),
("The Book of Trees","Book","Manuel Lima","2014","Princeton Architectural Press","history;hierarchy;diagrams","Eight hundred years of tree diagrams as a way of ordering knowledge.","https://www.goodreads.com/search?q=The+Book+of+Trees+Manuel+Lima",1,"active",K),
("The Book of Circles","Book","Manuel Lima","2017","Princeton Architectural Press","history;diagrams","The circle as a visual model across cultures and centuries.","https://www.goodreads.com/search?q=The+Book+of+Circles+Manuel+Lima",1,"active",K),
("The Infographic History of the World","Book","Valentina D'Efilippo & James Ball","2013","Collins","history;infographics","World history from the Big Bang onward, told in charts.","https://www.goodreads.com/search?q=Infographic+History+of+the+World",1,"active",K),
("Visualizing Complexity: Modular Information Design Handbook","Book","Nicole Lachenmeier & Darjan Hil (Superdot)","2022","Birkhäuser","information-design;method;teaching","A modular system of 80 elements for building information graphics; strong for teaching.","https://www.superdot.studio/visualizing-complexity-modular-information-design-handbook",1,"active",V),
("Observe, Collect, Draw! A Visual Journal","Book","Giorgia Lupi & Stefanie Posavec","2018","Princeton Architectural Press","data-humanism;workbook;teaching","A guided journal of prompts for collecting and drawing your own data. Good for first workshops.","https://www.goodreads.com/search?q=Observe+Collect+Draw",0,"active",K),
("Atlas of AI","Book","Kate Crawford","2021","Yale University Press","ai-ethics;extraction;power","AI as an extractive industry built from minerals, labour and classification.","https://yalebooks.yale.edu/book/9780300264630/atlas-of-ai/",0,"active",K),
("Living in Data","Book","Jer Thorp","2021","MCD / Farrar, Straus and Giroux","data-humanism;citizenship;ethics","A practitioner's case for data literacy as civic power.","https://www.jerthorp.com",0,"active",K),
("Data Action: Using Data for Public Good","Book","Sarah Williams","2020","MIT Press","civic-data;cities;activism","Civic Data Design Lab case studies on using data to change policy. Open access.","https://mitpress.mit.edu/9780262044196/data-action/",0,"active",K),
("Invisible Women","Book","Caroline Criado Perez","2019","Chatto & Windus","gender;data-gaps;bias","How a world designed on male-default data fails women. A book about the gender data gap.","https://www.goodreads.com/search?q=Invisible+Women+Criado+Perez",0,"active",K),
("Weapons of Math Destruction","Book","Cathy O'Neil","2016","Crown","algorithms;ethics;inequality","How opaque models at scale entrench inequality.","https://www.goodreads.com/search?q=Weapons+of+Math+Destruction",0,"active",K),
("Automating Inequality","Book","Virginia Eubanks","2018","St. Martin's Press","algorithms;welfare;ethics","How automated eligibility systems police and punish the poor in the US.","https://www.goodreads.com/search?q=Automating+Inequality+Eubanks",0,"active",K),
("Recoding America","Book","Jennifer Pahlka","2023","Metropolitan Books","civic-tech;government;policy","Why government technology fails, from the founder of Code for America. Close kin to Mike Flowers's world.","https://www.recodingamerica.us",0,"active",K),
("The Visual Display of Quantitative Information","Book","Edward Tufte","1983","Graphics Press","classic;statistics;information-design","The classic on data-ink, chartjunk and graphical integrity.","https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/",0,"active",K),
("Semiology of Graphics","Book","Jacques Bertin","1967","Esri Press (English ed.)","classic;theory;maps","The original grammar of visual variables: position, size, value, texture, colour, orientation, shape.","https://www.goodreads.com/search?q=Semiology+of+Graphics+Bertin",0,"active",K),
("How Charts Lie","Book","Alberto Cairo","2019","W. W. Norton","literacy;misinformation;statistics","Reading charts critically: truncated axes, bad data, misleading encodings.","https://www.albertocairo.com",0,"active",K),
("W. E. B. Du Bois's Data Portraits","Book","Whitney Battle-Baptiste & Britt Rusert (eds.)","2018","Princeton Architectural Press","history;race;information-design","The hand-drawn charts Du Bois's team made for the 1900 Paris Exposition, reproduced in full.","https://www.goodreads.com/search?q=Du+Bois+Data+Portraits",0,"active",K),
("Sorting Things Out","Book","Geoffrey C. Bowker & Susan Leigh Star","1999","MIT Press","classification;infrastructure;theory","Classification systems as political infrastructure. Pairs well with Data Feminism.","https://mitpress.mit.edu/9780262522953/sorting-things-out/",0,"active",K),
("Seeing Like a State","Book","James C. Scott","1998","Yale University Press","legibility;government;theory","How states simplify the world to make it measurable, and what goes wrong when they do.","https://www.goodreads.com/search?q=Seeing+Like+a+State",0,"active",K),
("'Raw Data' Is an Oxymoron","Book","Lisa Gitelman (ed.)","2013","MIT Press","theory;history","Essays arguing that data is always made, never found.","https://mitpress.mit.edu/9780262518284/raw-data-is-an-oxymoron/",0,"active",K),
("Info We Trust","Book","RJ Andrews","2019","Wiley","storytelling;history;information-design","An illustrated, idiosyncratic guide to data storytelling.","https://infowetrust.com",0,"active",K),
("Atlas of Remote Islands","Book","Judith Schalansky","2009","Penguin (English ed.)","maps;weird;narrative","Fifty islands mapped with one strange story each. Cartography as literature.","https://www.goodreads.com/search?q=Atlas+of+Remote+Islands",0,"active",K),
("The Art of Statistics","Book","David Spiegelhalter","2019","Pelican","statistics;literacy","Learning from data through real questions, with no formulas up front.","https://www.goodreads.com/search?q=The+Art+of+Statistics+Spiegelhalter",0,"active",K),
("The Ghost Map","Book","Steven Johnson","2006","Riverhead","history;maps;public-health","John Snow's 1854 cholera map and the birth of epidemiology.","https://www.goodreads.com/search?q=The+Ghost+Map",0,"active",K),

# ---------- PEOPLE ----------
("Giorgia Lupi","Person","Information designer; partner at Pentagram","","New York","data-humanism;information-design","Co-founded Accurat in Milan; coined 'Data Humanism'. Born in Italy.","https://giorgialupi.com",1,"active",K),
("Stefanie Posavec","Person","Designer, artist, author","","London","data-humanism;physicalisation;drawing","Hand-made, tactile and performative data work.","https://www.stefanieposavec.com",1,"active",K),
("Hans Rosling (1948–2017)","Person","Physician, statistician, co-founder of Gapminder","","Sweden","statistics;development;public-speaking","Animated bubble charts and the 2006 TED talk that made statistics a public spectacle.","https://www.gapminder.org/about/about-gapminder/hans-rosling/",1,"historical",K),
("César Hidalgo","Person","Physicist; director, Center for Collective Learning","","Toulouse / Budapest","complexity;economics","Creator of the Observatory of Economic Complexity and Data USA; formerly MIT Media Lab.","https://cesarhidalgo.com",1,"active",K),
("Manuel Lima","Person","Designer, author; founder of VisualComplexity.com","","London / New York","networks;history","Writes the history of diagrams as tools for thought.","https://www.visualcomplexity.com",1,"active",K),
("Valentina D'Efilippo","Person","Information designer, creative director","","London","information-design;data-art","Known for 'Poppy Field' (war deaths) and 'OddityViz' (Bowie's Space Oddity as data).","https://www.valentinadefilippo.co.uk",1,"active",K),
("Mike Flowers","Person","Data and analytics leader; NYC's first Chief Analytics Officer (2009–13)","","New York","civic-data;government;open-data","Founded the Mayor's Office of Data Analytics under Bloomberg; started as a Manhattan prosecutor. Now global head of data, AI and technology at K2 Integrity.","https://www.k2integrity.com",1,"active",V),
("Nicole Lachenmeier & Darjan Hil","Person","Co-founders of Superdot","","Basel","information-design;teaching","Swiss information designers, educators and hosts of On Data and Design.","https://www.superdot.studio",1,"active",V),
("Federica Fragapane","Person","Independent information designer","","Milan","information-design;data-art;italy","Delicate, organic visual languages for the UN, WHO, BBC and La Lettura. Work held at MoMA.","https://www.behance.net/FedericaFragapane",0,"active",V),
("Mona Chalabi","Person","Data journalist and illustrator","","New York / London","journalism;illustration","Hand-drawn charts that make statistics feel human; Pulitzer Prize for illustrated reporting (2023).","https://monachalabi.com",0,"active",K),
("Mimi Onuoha","Person","Artist and researcher","","Brooklyn","data-gaps;art;power","Makes absence visible: what isn't collected, and why. See 'The Library of Missing Datasets'.","https://mimionuoha.com",0,"active",K),
("Catherine D'Ignazio","Person","Associate Professor, MIT; director, Data + Feminism Lab","","Cambridge, MA","data-feminism;civic-data","Co-author of Data Feminism; also wrote 'Counting Feminicide' (2024).","https://www.kanarinka.com",0,"active",K),
("Jer Thorp","Person","Data artist, writer","","Canada / US","data-humanism;art","Former NYT data artist in residence; Library of Congress innovator in residence.","https://www.jerthorp.com",0,"active",K),
("Kate Crawford","Person","Researcher (AI and society)","","Sydney / New York","ai-ethics;art","Co-author, with Vladan Joler, of 'Anatomy of an AI System' and 'Calculating Empires'.","https://katecrawford.net",0,"active",K),
("Alberto Cairo","Person","Knight Chair in Visual Journalism, University of Miami","","Miami","journalism;literacy","Author of The Functional Art and How Charts Lie.","https://www.albertocairo.com",0,"active",K),
("Nadieh Bremer","Person","Data visualisation designer (Visual Cinnamon)","","Netherlands","data-art;d3","Hand-coded, intricate data art; co-authored 'Data Sketches' with Shirley Wu.","https://www.visualcinnamon.com",0,"active",K),
("Shirley Wu","Person","Data visualisation designer and artist","","San Francisco","data-art;d3","Co-author of 'Data Sketches'; makes data into physical and performative pieces.","https://shirleywu.studio",0,"active",K),
("Moritz Stefaner","Person","Founder, Truth & Beauty","","Germany","information-design;complexity","Long-running Data Stories podcast co-host; OECD Better Life Index.","https://truth-and-beauty.net",0,"active",K),
("Paolo Ciuccarelli","Person","Designer, professor at Northeastern; DensityDesign co-founder","","Boston / Milan","information-design;italy;research","Founded DensityDesign Lab at Politecnico di Milano.","https://camd.northeastern.edu",0,"active",K),
("Max Roser","Person","Economist; founder of Our World in Data","","Oxford","development;open-data","Built OWID into the reference for long-run global data.","https://ourworldindata.org/team",0,"active",K),
("Jeremy Singer-Vine","Person","Data journalist; author of Data Is Plural","","New York","datasets;journalism","Weekly newsletter of useful and curious datasets since 2015.","https://www.data-is-plural.com",0,"active",K),
("Sarah Williams","Person","Director, Civic Data Design Lab, MIT","","Cambridge, MA","civic-data;cities","Data for public action: 'Digital Matatus' mapped Nairobi's informal transit.","https://civicdatadesignlab.mit.edu",0,"active",K),
("Eyal Weizman","Person","Architect; founder of Forensic Architecture","","London","human-rights;spatial-analysis","Spatial and data reconstructions of state violence as evidence.","https://forensic-architecture.org",0,"active",K),
("Dietmar Offenhuber","Person","Professor, Northeastern University","","Boston","physicalisation;cities;research","Studies the materiality of data; author of 'Autographic Design' (2023).","https://offenhuber.net",0,"active",K),
("Vladan Joler","Person","Researcher, SHARE Foundation","","Novi Sad","ai-ethics;maps;power","Giant critical maps of tech infrastructure (with Kate Crawford).","https://labs.rs",0,"active",K),
("Mushon Zer-Aviv","Person","Designer, activist, educator","","Tel Aviv","activism;ethics","Data activism, open-source design, critical approaches to the dashboard.","https://mushon.com",0,"active",K),
("Florence Nightingale (1820–1910)","Person","Statistician, nurse","","London","history;public-health;classic","Her 1858 'rose' diagram changed military hospital policy. Early proof that charts persuade.","https://en.wikipedia.org/wiki/Florence_Nightingale",0,"historical",K),
("Otto & Marie Neurath","Person","Creators of Isotype","","Vienna / Oxford","history;pictograms;classic","Isotype (1920s–40s): a picture language for public statistics.","https://en.wikipedia.org/wiki/Isotype_(picture_language)",0,"historical",K),
("W. E. B. Du Bois (1868–1963)","Person","Sociologist, historian, activist","","Atlanta","history;race;classic","His 1900 data portraits of Black life in America remain startlingly modern.","https://en.wikipedia.org/wiki/W._E._B._Du_Bois",0,"historical",K),

# ---------- STUDIOS & LABS ----------
("Superdot – visualizing complexity","Studio & Lab","Nicole Lachenmeier & Darjan Hil","2011","Basel","information-design;teaching;physicalisation","Information design and data experience studio. Runs the 'On Data and Design' event series. Formerly YAAY.","https://www.superdot.studio",1,"active",V),
("Come ViVi Venezia (Superdot)","Studio & Lab","Superdot","2025","Venice","cities;overtourism;participatory","A month-long Venice residency mapping urban quality of life, mixing data with residents' lived experience. Good Design Award 2025. I could not confirm a book edition; see note.","https://good-design.org/projects/come-vivi-venezia-a-multidimensional-framework-for-urban-quality-of-life/",1,"active",V),
("Beyond Words Studio","Studio & Lab","Rebecca Conroy & Duncan Swain","","London","information-design;storytelling","Data design studio for reports, visual explainers and interactive pieces.","https://www.beyondwordsstudio.com",1,"active",V),
("Parallel","Studio & Lab","Parallel Intelligence Ltd.","","London","decision-intelligence;product;ai","Innovation consultancy for decision-making and analytics tools: situational awareness, AI products, decision intelligence. Clients include the BBC and The Guardian. Co-founded by Matthew Falla (formerly of Signal Noise).","https://parallel.systems",1,"active",V),
("Accurat","Studio & Lab","Co-founded by Giorgia Lupi, Gabriele Rossi, Simone Quadri","2011","Milan / New York","information-design;italy","Data-driven research, design and innovation; La Lettura's data visualisations.","https://www.accurat.it",0,"active",K),
("DensityDesign Lab","Studio & Lab","Politecnico di Milano","2004","Milan","research;italy;tools","Research lab behind RAWGraphs; visual tools for complex social issues.","https://densitydesign.org",0,"active",K),
("Domestic Data Streamers","Studio & Lab","Pau Garcia and team","2013","Barcelona","physicalisation;participatory;installation","Turns data into participatory installations, from public surveys to physical archives.","https://domesticstreamers.com",0,"active",K),
("Forensic Architecture","Studio & Lab","Goldsmiths, University of London","2010","London","human-rights;spatial-analysis;evidence","Investigates human rights violations with spatial, architectural and data analysis.","https://forensic-architecture.org",0,"active",K),
("Tactical Tech","Studio & Lab","NGO","2003","Berlin","digital-rights;activism;education","Data and technology for activists; 'The Glass Room' exhibitions on personal data.","https://tacticaltech.org",0,"active",K),
("Data4Change","Studio & Lab","Non-profit","","Global","human-rights;data-design;journalism","Connects human-rights organisations with data and design practitioners.","https://www.data4change.org",0,"active",K),
("Fathom Information Design","Studio & Lab","Founded by Ben Fry","2010","Boston","information-design;tools","Studio of Processing co-creator Ben Fry; science, health and media visualisation.","https://fathom.info",0,"active",K),
("Stamen","Studio & Lab","Founded by Eric Rodenbeck","2001","San Francisco","maps;cartography","Pioneering map and data design studio; the original watercolor and toner map tiles.","https://stamen.com",0,"active",K),
("Pitch Interactive","Studio & Lab","Wesley Grubbs & team","2006","Berkeley","information-design;journalism","Interactive data work; 'Out of Sight, Out of Mind' on drone strikes.","https://pitchinteractive.com",0,"active",K),
("Periscopic","Studio & Lab","","2004","Portland","activism;storytelling","'Do good with data'; known for 'U.S. Gun Deaths: stolen years'.","https://periscopic.com",0,"active",K),
("Truth & Beauty","Studio & Lab","Moritz Stefaner","","Germany","complexity;information-design","Data visualisation for exploring complex information.","https://truth-and-beauty.net",0,"active",K),
("Visual Cinnamon","Studio & Lab","Nadieh Bremer","","Netherlands","data-art","Freelance data art and visualisation studio.","https://www.visualcinnamon.com",0,"active",K),
("The Visual Agency","Studio & Lab","","2006","Milan","information-design;italy","Milanese information design agency (Matteo Bonera spoke at Italian dataviz events).","https://thevisualagency.com",0,"active",K),
("Ferdio","Studio & Lab","","2012","Copenhagen","information-design;tools","Infographics agency; maintains the Data Viz Project reference catalogue.","https://ferdio.com",0,"active",K),
("CLEVER°FRANKE","Studio & Lab","","2008","Utrecht","data-experience;dashboards","Data-driven experiences and dashboards.","https://www.cleverfranke.com",0,"active",K),
("Interactive Things","Studio & Lab","","2010","Zurich","information-design;journalism","Swiss studio for data visualisation and digital products.","https://www.interactivethings.com",0,"active",K),
("Studio Terp","Studio & Lab","Sonja Kuijpers","","Netherlands","data-art;illustration","Poetic, illustrative data visualisation.","https://www.studioterp.nl",0,"active",K),
("Parabole Studio","Studio & Lab","Evelina Parrou","","London","information-design","Data visualisation and information design studio.","https://parabole.studio",0,"active",K),
("Applied Works","Studio & Lab","Joe Sharpe & team","","London","product;data-products","Design studio for data-heavy digital products.","https://applied.works",0,"active",K),
("Koponen+Hildén","Studio & Lab","Juuso Koponen & Jonatan Hildén","","Helsinki","information-design;teaching","Information design studio; authors of 'Data Visualization Handbook'.","https://www.koponenhilden.fi",0,"active",K),
("MIT Senseable City Lab","Studio & Lab","Directed by Carlo Ratti","2004","Cambridge, MA","cities;sensing;research","Data on how cities move and breathe: trash tracking, mobility, sensing.","https://senseable.mit.edu",0,"active",K),
("Center for Collective Learning","Studio & Lab","César Hidalgo","","Toulouse / Budapest","complexity;economics;research","Hidalgo's research group on collective learning and economic complexity.","https://centerforcollectivelearning.org",0,"active",K),
("Data Justice Lab","Studio & Lab","Cardiff University","2017","Cardiff","data-justice;surveillance;research","Research on datafication and social justice; runs the Data Justice Conference.","https://datajusticelab.org",0,"active",K),
("Pentagram","Studio & Lab","Partnership","1972","Global","design;branding","Design partnership where Giorgia Lupi leads data-driven work.","https://www.pentagram.com",0,"active",K),

# ---------- FESTIVALS & CONFERENCES ----------
("DataFest Tbilisi","Festival & Conference","Organised by ForSet","2017","Tbilisi, Georgia","multidisciplinary;ai;human-rights","Largest data festival in Eastern Europe and Central Asia. 10th edition 26–28 November 2026, with kids and 65+ programmes.","https://www.datafest.ge",1,"active",V),
("re:publica","Festival & Conference","","2007","Berlin","digital-society;internet;politics","Festival on digital society, internet culture and politics, held every spring.","https://re-publica.com",1,"active",K),
("RightsCon","Festival & Conference","Access Now","2011","Rotating","human-rights;digital-rights","The main summit on human rights in the digital age. The 2026 edition in Lusaka was cancelled days before opening; 'RightsCon Continues' events followed.","https://www.rightscon.org",1,"active",V),
("On Data and Design","Festival & Conference","Superdot","","Basel / online","information-design;community","Superdot's meetup and talk series on data and design, streamed live on YouTube. Likely the 'Data & Design' series you mean.","https://www.meetup.com/ondataanddesign-switzerland/",1,"active",V),
("Information+ Conference","Festival & Conference","Rotating universities","2016","Rotating","information-design;research;practice","Biennial conference for researchers and practitioners. Last held in Boston, Nov 2025.","https://informationplusconference.com",0,"active",V),
("Outlier","Festival & Conference","Data Visualization Society","2021","Online","dataviz;community","DVS's annual conference; 2026 edition was online in June.","https://www.outlierconf.com",0,"active",V),
("IEEE VIS","Festival & Conference","IEEE","1990","Rotating","research;academic","The main academic visualisation conference.","https://ieeevis.org",0,"active",K),
("Visualising Climate","Festival & Conference","Copernicus / ECMWF","","Bologna, Italy","climate;italy","Climate data visualisation event; the 2026 edition was in Bologna in November.","https://climate.copernicus.eu/visualising-climate-2026",0,"active",V),
("MozFest","Festival & Conference","Mozilla Foundation","2010","Barcelona (recent)","internet-health;ai-ethics;civic-data","Festival for a healthier internet; tech ethics, civic data, digital rights.","https://www.mozillafestival.org",0,"active",V),
("Malofiej","Festival & Conference","SND-E / University of Navarra","1993","Pamplona","journalism;infographics","Long-running awards and summit for news infographics.","https://www.malofiejgraphics.com",0,"active",K),
("International Journalism Festival","Festival & Conference","","2007","Perugia, Italy","journalism;data-journalism;italy","Free journalism festival in Perugia with a strong data-journalism track.","https://www.journalismfestival.com",0,"active",K),
("Global Investigative Journalism Conference","Festival & Conference","GIJN","2001","Rotating","journalism;investigation","Where data and investigative journalists share methods.","https://gijn.org",0,"active",K),
("NICAR","Festival & Conference","Investigative Reporters and Editors","","US, rotating","data-journalism;tools","The data-journalism conference: scraping, analysis, newsroom tooling.","https://www.ire.org/training/conferences/",0,"active",K),
("CPDP – Computers, Privacy & Data Protection","Festival & Conference","","2007","Brussels","privacy;policy;gdpr","Where EU data protection policy is argued in public. Relevant to GDPR work.","https://www.cpdpconferences.org",0,"active",K),
("Chaos Communication Congress","Festival & Conference","Chaos Computer Club","1984","Hamburg","hacking;digital-rights","Annual end-of-December gathering on security, technology and society.","https://events.ccc.de",0,"active",K),
("ACM FAccT","Festival & Conference","ACM","2018","Rotating","ai-ethics;fairness;research","Fairness, accountability and transparency in socio-technical systems.","https://facctconference.org",0,"active",K),
("Data Justice Conference","Festival & Conference","Data Justice Lab","2018","Cardiff","data-justice;surveillance","Research and activism on datafication and justice.","https://datajusticelab.org",0,"active",K),
("Ars Electronica Festival","Festival & Conference","","1979","Linz","art;technology;data-art","Art, technology and society; frequent home for data and AI art.","https://ars.electronica.art",0,"active",K),
("KIKK Festival","Festival & Conference","","2011","Namur, Belgium","creative-tech;art","Digital and creative culture festival with talks and installations.","https://www.kikk.be",0,"active",K),
("csv,conf","Festival & Conference","Community-run","2014","Rotating","open-data;community","Community conference for data makers, librarians, scientists and coders.","https://csvconf.com",0,"active",K),
("UN World Data Forum","Festival & Conference","UN Statistical Commission","2017","Rotating","official-statistics;development","Global forum for official statistics and sustainable development data.","https://unstats.un.org/UNSDWebsite/undataforum/",0,"active",K),
("Open Data Day","Festival & Conference","Open Knowledge Foundation","2010","Worldwide","open-data;community","Annual day of local open-data events around the world.","https://opendataday.org",0,"active",K),
("Eyeo Festival","Festival & Conference","","2011","Minneapolis","creative-coding;dataviz","Hugely influential creative-coding and dataviz gathering. Talk archive on Vimeo is still worth mining.","https://www.eyeofestival.com",0,"archived",K),
("Resonate","Festival & Conference","","2012","Belgrade","creative-tech;art","Belgrade digital-culture festival; documented as no longer running. Keep for talk archives only.","https://en.wikipedia.org/wiki/Resonate_(festival)",0,"archived",V),

# ---------- DATA PORTALS ----------
("data.europa.eu","Data Portal","European Union","","EU","open-data;europe","Official EU portal aggregating datasets from EU institutions and national portals.","https://data.europa.eu",0,"active",K),
("Eurostat","Data Portal","European Commission","","Luxembourg","official-statistics;europe","EU statistics down to NUTS regional level, including tourism nights by region.","https://ec.europa.eu/eurostat",0,"active",K),
("ISTAT – Esploradati","Data Portal","Istituto Nazionale di Statistica","","Italy","official-statistics;italy","Italian national statistics (demography, tourism, economy) via the Esploradati tool.","https://esploradati.istat.it",0,"active",K),
("dati.gov.it","Data Portal","AgID","","Italy","open-data;italy","Italy's national open-data catalogue, aggregating regional and municipal portals.","https://www.dati.gov.it",0,"active",K),
("Open Data Lombardia","Data Portal","Regione Lombardia","","Lombardy","open-data;italy;regional","Regional open data, including tourism and mobility datasets. Useful for Bergamo work.","https://www.dati.lombardia.it",0,"active",K),
("World Bank Open Data","Data Portal","World Bank","","Global","development;economics","Development indicators for every country, with a clean API.","https://data.worldbank.org",0,"active",K),
("UNdata","Data Portal","United Nations Statistics Division","","Global","official-statistics","Single entry point for UN statistical databases.","https://data.un.org",0,"active",K),
("OECD Data Explorer","Data Portal","OECD","","Paris","economics;policy","OECD statistics on economy, society, environment and wellbeing.","https://data-explorer.oecd.org",0,"active",K),
("Humanitarian Data Exchange (HDX)","Data Portal","UN OCHA","2014","Global","humanitarian;crisis","Open platform for humanitarian data across crises and agencies.","https://data.humdata.org",0,"active",K),
("data.gov","Data Portal","US Government","2009","United States","open-data;government","US federal open-data catalogue.","https://data.gov",0,"active",K),
("NYC Open Data","Data Portal","City of New York","2012","New York","civic-data;cities","Born out of the Mike Flowers-era open-data push; one of the richest city portals anywhere.","https://opendata.cityofnewyork.us",0,"active",K),
("data.gov.uk","Data Portal","UK Government","2010","United Kingdom","open-data;government","UK public-sector open data.","https://www.data.gov.uk",0,"active",K),
("Copernicus Data Space","Data Portal","European Space Agency / EU","","EU","climate;earth-observation","Free Sentinel satellite imagery and Earth observation products.","https://dataspace.copernicus.eu",0,"active",K),
("NASA Earthdata","Data Portal","NASA","","US","climate;earth-observation","NASA's Earth science data archive.","https://www.earthdata.nasa.gov",0,"active",K),

# ---------- DATASET SOURCES ----------
("Our World in Data","Dataset Source","Global Change Data Lab / University of Oxford","2011","Oxford","development;open-data;research","Research and data on the world's largest problems, all downloadable with sources documented.","https://ourworldindata.org",0,"active",K),
("Gapminder","Dataset Source","Gapminder Foundation","2005","Stockholm","development;education","Rosling's foundation: Gapminder tools, data and the 'Worldview Upgrader' quizzes.","https://www.gapminder.org",1,"active",K),
("Observatory of Economic Complexity (OEC)","Dataset Source","César Hidalgo / Datawheel","2011","Global","trade;complexity;economics","Explore what every country makes and trades; the applied form of Why Information Grows.","https://oec.world",1,"active",K),
("Data Is Plural","Dataset Source","Jeremy Singer-Vine","2015","Newsletter","datasets;weird","Weekly newsletter of datasets, with a searchable archive spreadsheet of more than 1,000 entries.","https://www.data-is-plural.com",0,"active",K),
("Google Dataset Search","Dataset Source","Google","2018","Global","search","Search engine across dataset repositories.","https://datasetsearch.research.google.com",0,"active",K),
("Kaggle Datasets","Dataset Source","Google","2010","Global","datasets;ml","Huge community dataset library. Quality varies; check provenance.","https://www.kaggle.com/datasets",0,"active",K),
("awesome-public-datasets","Dataset Source","Community (GitHub)","","GitHub","datasets;open-data","Topic-sorted list of high-quality public datasets.","https://github.com/awesomedata/awesome-public-datasets",0,"active",K),
("TidyTuesday","Dataset Source","R4DS community","2018","GitHub","datasets;teaching;community","A new dataset every week for practice. Excellent for students.","https://github.com/rfordatascience/tidytuesday",0,"active",K),
("ACLED","Dataset Source","Armed Conflict Location & Event Data","","Global","conflict;human-rights","Disaggregated data on political violence and protest. Registration required.","https://acleddata.com",0,"active",K),
("ICIJ Offshore Leaks Database","Dataset Source","International Consortium of Investigative Journalists","","Global","journalism;finance;investigation","Searchable entities from the Panama, Paradise and Pandora Papers.","https://offshoreleaks.icij.org",0,"active",K),
("OCCRP Aleph","Dataset Source","Organized Crime and Corruption Reporting Project","","Global","journalism;investigation","Search engine across leaks, registries and public records for investigators.","https://aleph.occrp.org",0,"active",K),
("OpenStreetMap","Dataset Source","OpenStreetMap Foundation","2004","Global","maps;open-data;cities","The open, editable map of the world; the base for street-width work.","https://www.openstreetmap.org",0,"active",K),
("Wikidata","Dataset Source","Wikimedia Foundation","2012","Global","knowledge-graph;open-data","Structured, linked open data behind Wikipedia, queryable with SPARQL.","https://www.wikidata.org",0,"active",K),
("IPUMS","Dataset Source","University of Minnesota","","Global","census;demography","Harmonised census and survey microdata across countries and centuries.","https://www.ipums.org",0,"active",K),
("Global Forest Watch","Dataset Source","World Resources Institute","2014","Global","climate;forests","Near-real-time forest monitoring data.","https://www.globalforestwatch.org",0,"active",K),
("Zenodo","Dataset Source","CERN / OpenAIRE","2013","Global","research;open-science","Open repository for research datasets with DOIs.","https://zenodo.org",0,"active",K),

# ---------- WEIRD DATASETS ----------
("The Library of Missing Datasets","Weird Dataset","Mimi Onuoha","2016","Installation","data-gaps;art","A filing cabinet of empty folders: datasets that should exist but don't. An absence as a dataset.","https://mimionuoha.com/the-library-of-missing-datasets",0,"active",K),
("Dear Data postcards","Weird Dataset","Lupi & Posavec","2015","Collection","data-humanism;personal-data","104 postcards logging small things: complaints, laughter, doors opened. Held by MoMA.","https://www.dear-data.com/all",1,"active",K),
("Dollar Street","Weird Dataset","Gapminder","","Global","development;photography","Photos of homes worldwide, sorted by income: toothbrushes, stoves, beds.","https://www.gapminder.org/dollar-street",0,"active",K),
("Central Park Squirrel Census","Weird Dataset","The Squirrel Census","2018","New York","weird;cities;citizen-science","Volunteers counted every squirrel in Central Park, noting fur colour and behaviour. On NYC Open Data.","https://www.thesquirrelcensus.com",0,"active",K),
("NYC Dog Licensing Dataset","Weird Dataset","NYC Department of Health","","New York","weird;cities","Every licensed dog in NYC by name, breed and ZIP code.","https://data.cityofnewyork.us",0,"active",K),
("Melbourne Urban Forest (trees with email addresses)","Weird Dataset","City of Melbourne","2013","Melbourne","cities;trees;weird","Trees got IDs and email addresses for fault reporting. People wrote them love letters instead.","https://data.melbourne.vic.gov.au",0,"active",K),
("NYC Street Tree Census","Weird Dataset","NYC Parks","2015","New York","cities;trees","Every street tree in NYC: species, health, size.","https://opendata.cityofnewyork.us",0,"active",K),
("NYPL 'What's on the Menu?'","Weird Dataset","New York Public Library","2011","New York","history;food","Transcribed historical restaurant menus: dishes, prices, decades.","https://menus.nypl.org",0,"active",K),
("Spurious Correlations","Weird Dataset","Tyler Vigen","2014","Web","statistics;humour;teaching","Absurd correlations, like cheese consumption against bedsheet deaths. Good for teaching correlation versus causation.","https://www.tylervigen.com/spurious-correlations",0,"active",K),
("Meteorite Landings","Weird Dataset","NASA / The Meteoritical Society","","Global","space;weird","About 45,000 known meteorite landings with mass, class and location.","https://data.nasa.gov",0,"active",K),
("NUFORC UFO Sightings","Weird Dataset","National UFO Reporting Center","","US","weird;citizen-reports","Decades of self-reported UFO sightings with free-text descriptions. Unverified by definition.","https://nuforc.org",0,"active",K),
("FAA Wildlife Strike Database","Weird Dataset","Federal Aviation Administration","1990","US","weird;aviation","Every reported collision between aircraft and wildlife.","https://wildlife.faa.gov",0,"active",K),
("Global Shark Attack File","Weird Dataset","Shark Research Institute","","Global","weird;nature","Historical incidents of shark-human interaction.","https://www.sharkattackfile.net",0,"active",K),
("Old Bailey Online","Weird Dataset","Universities of Sheffield, Hertfordshire et al.","","London","history;justice","197,745 criminal trials from London's central court, 1674–1913.","https://www.oldbaileyonline.org",0,"active",K),
("The Pudding: Film Dialogue by Gender","Weird Dataset","The Pudding","2016","Web","gender;film;data-gaps","Lines of dialogue by gender across 2,000 screenplays.","https://pudding.cool/2017/03/film-dialogue/",0,"active",K),
("Every Noise at Once","Weird Dataset","Glenn McDonald","","Web","music;maps","A scatterplot of about 6,000 music genres. No longer updated since the creator left Spotify.","https://everynoise.com",0,"archived",K),
("MoMA Collection (GitHub)","Weird Dataset","Museum of Modern Art","","New York","art;museums","Metadata for 130,000+ works: titles, dimensions, acquisition dates.","https://github.com/MuseumofModernArt/collection",0,"active",K),
("Rebrickable LEGO Database","Weird Dataset","Rebrickable","","Web","weird;toys","Every LEGO set, part and colour since 1949.","https://rebrickable.com/downloads/",0,"active",K),

# ---------- WEBSITES & PUBLICATIONS ----------
("The Pudding","Website & Publication","","2017","Web","storytelling;culture","Visual essays on culture, explained with data.","https://pudding.cool",0,"active",K),
("Nightingale","Website & Publication","Data Visualization Society","2019","Web / print","dataviz;community","DVS's journal of data visualisation, online and in print.","https://nightingaledvs.com",0,"active",V),
("FlowingData","Website & Publication","Nathan Yau","2007","Web","dataviz;tutorials","Long-running site on visualisation, with tutorials.","https://flowingdata.com",0,"active",K),
("Information is Beautiful","Website & Publication","David McCandless","2009","Web","infographics","Infographics and the Information is Beautiful Awards showcase.","https://informationisbeautiful.net",0,"active",K),
("VisualComplexity.com","Website & Publication","Manuel Lima","2005","Web","networks;archive","Archive of network visualisation projects. Mostly historical now.","https://www.visualcomplexity.com",1,"archived",K),
("Data Viz Project","Website & Publication","Ferdio","","Web","reference;teaching","Catalogue of chart types by shape, function and input.","https://datavizproject.com",0,"active",K),
("Datawrapper Blog","Website & Publication","Datawrapper (Lisa Charlotte Muth et al.)","","Berlin","dataviz;craft","Sharp writing on chart craft, colour and readability.","https://www.datawrapper.de/blog",0,"active",K),
("Visualising Data","Website & Publication","Andy Kirk","","UK","dataviz;events;community","Resources, an annual events list and the Explore Explain series.","https://visualisingdata.com",0,"active",V),
("Exposing the Invisible","Website & Publication","Tactical Tech","","Web","investigation;human-rights","Guides and kits for investigating with data and open sources.","https://exposingtheinvisible.org",0,"active",K),
("Public Data Lab","Website & Publication","Research network","","Europe","research;methods","Network exploring what public data means; 'A Field Guide to Fake News'.","https://publicdatalab.org",0,"active",K),

# ---------- VIDEO & PODCAST ----------
("On Data and Design (YouTube)","Video & Podcast","Superdot","","YouTube","information-design;talks","Recorded sessions of Superdot's 'On Data and Design' series. Match for 'Data & Design YouTube series'.","https://www.meetup.com/ondataanddesign-switzerland/",1,"active",V),
("The best stats you've ever seen (TED 2006)","Video & Podcast","Hans Rosling","2006","TED","statistics;public-speaking","The talk that launched a thousand bubble charts.","https://www.ted.com/talks/hans_rosling_the_best_stats_you_ve_ever_seen",1,"active",K),
("The Joy of Stats (BBC)","Video & Podcast","Hans Rosling","2010","BBC Four","statistics;documentary","Includes the famous 200 countries in 4 minutes sequence.","https://www.gapminder.org/videos/the-joy-of-stats/",1,"active",K),
("Explore Explain","Video & Podcast","Andy Kirk","2020","Video & podcast","dataviz;process","Long-form conversations on the design story behind single projects. Season 5 opened with Beyond Words.","https://visualisingdata.com/podcast/",0,"active",V),
("Data Stories","Video & Podcast","Enrico Bertini & Moritz Stefaner","2012","Podcast","dataviz;interviews","The longest-running dataviz podcast.","https://datastori.es",0,"active",K),
("PolicyViz Podcast","Video & Podcast","Jon Schwabish","","Podcast","dataviz;policy","Interviews on dataviz and policy communication; episode 263 features Superdot.","https://policyviz.com/podcast/",0,"active",V),
]

from additions import add
from urllib.parse import quote_plus
rows = rows + add
rows = [ (r[:7] + (r[7] or "https://duckduckgo.com/?q="+quote_plus(r[0]+" "+r[2]),) + r[8:10] + (("no link confirmed; search link" if not r[7] else r[10]),)) for r in rows ]
cols = ["name","category","who","year","place","tags","note","url","seed","status","verified"]
recs = [dict(zip(cols, r)) for r in rows]
for i, r in enumerate(recs, 1):
    r["id"] = i
    r["tags"] = [t for t in r["tags"].split(";") if t]
    r["seed"] = bool(r["seed"])

from catalogue import merge
recs = merge(recs)
from taxonomy import clean
recs = clean(recs)
# --- privacy for people: no contact links, no locations (places, region tags, nationality/birthplace notes) ---
from urllib.parse import quote_plus as _q
PERSON_NOTES = {
 "Giorgia Lupi": "Co-founded Accurat; coined 'Data Humanism'.",
 "Nicole Lachenmeier & Darjan Hil": "Information designers, educators and hosts of On Data and Design.",
 "Isabel Meirelles": "Author of Design for Information.",
 "Enrico Bertini": "Visualisation researcher; co-host of Data Stories.",
 "Jacopo Ottaviani": "Data journalist leading data work across Code for Africa's network.",
 "Rasagy Sharma": "Information designer; Viz Chitra community.",
 "Gurman Bhatia": "Graphics for Reuters and others.",
 "Tiziana Alocci": "Information designer and data artist.",
 "Chimdi Nwosu": "Practitioner and DVS community voice.",
 "Paola Villarreal": "Civic data work, including with the ACLU.",
 "Carlo Ratti": "Architect; curated the 2025 Venice Architecture Biennale.",
 "Donato Ricci": "Designer working on controversy mapping and digital methods.",
}
for r in recs:
    if r["category"] != "Person": continue
    r["place"] = ""
    keep = [i for i, f in enumerate(r["tag_families"]) if f != "regions"]
    r["tags"] = [r["tags"][i] for i in keep]; r["tag_families"] = [r["tag_families"][i] for i in keep]
    assert r["family"] != "regions", r["name"]
    if "linkedin.com" in r["url"]:
        r["url"] = "https://duckduckgo.com/?q=" + _q(r["name"] + " " + r["who"]); r["verified"] = "no link confirmed; search link"
    if r["name"] in PERSON_NOTES: r["note"] = PERSON_NOTES[r["name"]]
assert set(PERSON_NOTES) <= {r["name"] for r in recs if r["category"]=="Person"}

for i, r in enumerate(recs, 1): r["id"] = i
names = [r["name"] for r in recs]
assert len(names) == len(set(names)), "duplicate names"

json.dump(recs, open("data.json","w"), ensure_ascii=False, indent=1)
with open("data.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    cols2=cols+["family","source"]
    w.writerow(["id"]+cols2)
    for r in recs:
        w.writerow([r["id"]]+[ ";".join(r[c]) if c=="tags" else r[c] for c in cols2])

from collections import Counter
print(len(recs), Counter(r["category"] for r in recs), sum(r["seed"] for r in recs), Counter(r["verified"] for r in recs))
