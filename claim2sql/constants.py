from os import path
from shared.template import Template

APP_PATH = path.dirname(path.realpath(__file__))
APP_ENDPOINT = "/claimbuster"
APP_ENDPOINT_PARTS = {x for x in APP_ENDPOINT.split("/") if x}
APP_BASE_PATH = APP_ENDPOINT.split("/")[-1]
template = Template(APP_ENDPOINT, APP_ENDPOINT_PARTS, APP_BASE_PATH, "claimbuster", "templates")
IDIR_VALID_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0", f"localhost:5001", f"127.0.0.1:5001", f"0.0.0.0:5001",
                    "idir.uta.edu", "192.168.1.2", "192.168.1.13"]

PRESS_ARTICLES = [
    {
        "link_url": "http://mediashift.org/2017/10/fact-checking-army-waging-war-fake-news/",
        "image_url": "img/mediashift.jpg",
        "title_text": "The Fact-Checking Army Waging War on Fake News"
    },
    {
        "link_url": "http://policyoptions.irpp.org/magazines/july-2017/how-the-world-gets-its-facts-straight/",
        "image_url": "img/policy_options_logo.PNG",
        "title_text": "How the world gets its facts straight"
    },
    {
        "link_url": "https://www.dallasnews.com/news/higher-education/2017/07/20/professors-ut-arlington-ut-dallas-join-forces-fight-fake-news",
        "image_url": "img/dallas-news.png",
        "title_text": "Professors from UT-Arlington, UT-Dallas join forces to fight fake news"
    },
    {
        "link_url": "https://techxplore.com/news/2017-06-interdisciplinary-team-fake-news.html",
        "image_url": "img/tech_xplore_logo.png",
        "title_text": "Interdisciplinary team to construct computer program to identify fake news"
    },
    {
        "link_url": "http://mediashift.org/2017/03/sxsw-2017-embattled-journalism-in-focus/",
        "image_url": "img/mediashift.jpg",
        "title_text": "SXSW 2017: Embattled Journalism in Focus"
    },
    {
        "link_url": "http://www.theplaidzebra.com/government-transparency-website-keeps-track-state-legislators/",
        "image_url": "img/plaidzebra.png",
        "title_text": "Digital Democracy: government transparency website keeps track of state legislators"
    },
    {
        "link_url": "https://www.theguardian.com/science/2017/jan/31/fake-news-and-fact-checking-trump-is-demonstrating-how-to-outsmart-an-ai-artificial-intelligence",
        "image_url": "img/the-guardian.jpg",
        "title_text": "Fake news and fact-checking: Trump is demonstrating how to outsmart an AI"
    },
    {
        "link_url": "http://newatlas.com/how-to-fix-fake-news-problem/47800/",
        "image_url": "img/newatlas.png",
        "title_text": "How do you solve fake news problem in the post-truth era?"
    },
    {
        "link_url": "https://www.wired.com/2017/02/soon-bots-will-spying-state-lawmakers-every-move/",
        "image_url": "img/wired.png",
        "title_text": "A Heroic AI Will Let You Spy on Your Lawmakers’ Every Word"
    },
    {
        "link_url": "http://www.poynter.org/2016/fail-and-move-on-lessons-from-automated-fact-checking-experiments/429232/",
        "image_url": "img/poynter.jpg",
        "title_text": "Fail and move on: Lessons from automated fact-checking experiments"
    },
    {
        "link_url": "http://www.newstatesman.com/2016/08/post-truth-v-tech-could-machines-help-us-call-out-politicians-and-journalists-lies",
        "image_url": "img/newstatesman.png",
        "title_text": "Post-truth v tech: could machines help us call out politicians’ and journalists’ lies?"
    },
    {
        "link_url": "https://medium.com/journalism-innovation/journalism-and-the-machines-what-claimbuster-told-me-about-australian-politics-e3fc0c27cd6a#.yswocsbvr",
        "image_url": "img/tow.jpeg",
        "title_text": "Journalism and the machines: what ClaimBuster told me about Australian politics"
    },
    {
        "link_url": "http://www.poynter.org/2016/report-automated-fact-checking-is-coming-and-soon/426370/",
        "image_url": "img/poynter.jpg",
        "title_text": "Report: Automated fact-checking is coming (and soon)"
    },
    {
        "link_url": "http://nordicapis.com/automated-fact-checking-the-holy-grail-of-political-communication/",
        "image_url": "img/nordic-apis.jpg",
        "title_text": "Automated Fact Checking: The Holy Grail of Political Communication"
    },
    {
        "link_url": "http://www.theguardian.com/commentisfree/2016/apr/19/is-that-a-fact-checking-politicians-statements-just-got-a-whole-lot-easier?CMP=share_btn_link",
        "image_url": "img/the-guardian.jpg",
        "title_text": "Is that a fact? Checking politicians' statements just got a whole lot easier"
    },
    {
        "link_url": "http://niemanreports.org/articles/the-future-of-political-fact-checking/",
        "image_url": "img/nieman.svg",
        "title_text": "The Future of Political Fact-Checking"
    },
    {
        "link_url": "https://www.journalism.co.uk/news/what-would-an-automated-future-look-like-for-verification-in-the-newsroom-/s2/a626862/",
        "image_url": "img/journalism.gif",
        "title_text": "What would an automated future look like for verification in the newsroom?"
    },
    {
        "link_url": "http://www.poynter.org/2016/fact-checking-2-0-teaching-computers-how-to-spot-lies/404501/",
        "image_url": "img/poynter.jpg",
        "title_text": "Fact-checking 2.0: Teaching computers how to spot lies"
    },
    {
        "link_url": "http://www.poynter.org/2016/poynter-and-duke-to-hold-conference-on-automated-fact-checking/392559/",
        "image_url": "img/poynter.jpg",
        "title_text": "Poynter and Duke to hold conference on automated fact-checking"
    },
    {
        "link_url": "http://www.wired.it/attualita/media/2016/04/08/futuro-fact-checking-sempre-automatizzato/",
        "image_url": "img/wired.png",
        "title_text": "Il fact-checking del futuro? Sempre più automatico"
    },
    {
        "link_url": "http://www.zdnet.co.kr/column/column_view.asp?artice_id=20160404112223",
        "image_url": "img/zdnet.gif",
        "title_text": "사실확인해주는 컴퓨터…기자들 친구될까"
    },
    {
        "link_url": "http://www.theshorthorn.com/news/graduate-students-work-to-help-make-voting-process-easier/article_b7acf48c-c2e8-11e5-9091-d7aedf40fb3e.html",
        "image_url": "img/shorthorn.png",
        "title_text": "Graduate students work to help make voting process easier"
    },
    {
        "link_url": "https://web.archive.org/web/20180114150157/http://www.star-telegram.com:80/opinion/editorials/article59390066.html",
        "image_url": "img/star-telegram.jpg",
        "title_text": "UTA project will bust claims of candidates"
    },
    {
        "link_url": "http://www.nbcdfw.com/news/local/New-Software-Developed-at-UTA-Tracks-Candidates-Statements-364565851.html",
        "image_url": "img/nbcdfw.jpg",
        "title_text": "New Software Developed at UTA Tracks Candidates Statements"
    },
    {
        "link_url": "https://www.newscientist.com/article/mg22830473-000-text-detective-can-unmask-the-secret-influencers-behind-us-laws/",
        "image_url": "img/newscientist.png",
        "title_text": "Text detective can unmask the secret influencers behind US laws"
    },
    {
        "link_url": "http://www.catchnews.com/science-technology/the-prototype-fund-just-funded-20-amazing-projects-to-revolutionise-media-and-governance-1446739013.html",
        "image_url": "img/catchnews.png",
        "title_text": "The Prototype Fund just funded 20 amazing projects to revolutionise media"
    },
    {
        "link_url": "https://knightfoundation.org/articles/20-ideas-receive-support-knight-prototype-fund-media-and-information-projects/",
        "image_url": "img/kf.jpg",
        "title_text": "20 ideas receive support from Knight Prototype Fund for media and information projects"
    },
    {
        "link_url": "https://www.poynter.org/fact-checking/2015/the-holy-grail-of-computational-fact-checking-and-what-we-can-do-in-the-meantime/",
        "image_url": "img/poynter.jpg",
        "title_text": "The ‘Holy Grail’ of computational fact checking – and what we can do in the meantime"
    },
    {
        "link_url": "https://medium.com/1st-draft/automated-fact-checking-and-verification-will-only-happen-if-organizations-other-than-newsrooms-can-84cf40689924#.vkhtb7o0j",
        "image_url": "img/firstdraft.png",
        "title_text": "In search of fact checking’s ‘Holy Grail’: News outlets might not get there alone"
    },
    {
        "link_url": "https://www.statesman.com/story/news/2016/09/23/will-robots-take-over-fact-checking-the-information-overload/10048661007/",
        "image_url": "img/aas.png",
        "title_text": "...ClaimBuster ex­am­ines any tran­script to find sen­tences that should be fact checked"
    },
    {
        "link_url": "http://www.americanpressinstitute.org/fact-checking-project/the-week-in-fact-checking-introducing-mr-twitter-and-a-governors-hissy-fit/",
        "image_url": "img/apr.png",
        "title_text": "A professor at the University of Texas explains to the Austin-American Statesman how his “Claim-Buster” software could work during presidential debates"
    },
    {
        "link_url": "http://www.politifact.com/texas/article/2015/aug/18/robots-feeding-fact-checks-soon/",
        "image_url": "img/politifact.png",
        "title_text": "Li, a University of Texas-Arlington professor, is getting closer to helping journalists determine which presidential debate statements warrant fact-checking"
    }
]
