from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = "/sdcard/Download/Mohamed_Ramadan_Elnemer_CV.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=35, bottomMargin=35)
styles = getSampleStyleSheet()

t_style = ParagraphStyle('T', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=20, textColor=colors.HexColor('#1a365d'), alignment=1, spaceAfter=4)
sub_style = ParagraphStyle('Sub', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, textColor=colors.HexColor('#2b6cb0'), alignment=1, spaceAfter=4)
c_style = ParagraphStyle('C', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, textColor=colors.HexColor('#4a5568'), alignment=1, spaceAfter=12)
sec_style = ParagraphStyle('Sec', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=11, textColor=colors.HexColor('#1a365d'), spaceBefore=10, spaceAfter=4)
b_style = ParagraphStyle('B', parent=styles['Normal'], fontName='Helvetica', fontSize=9, textColor=colors.HexColor('#2d3748'), leading=13, spaceAfter=4)

story = [
    Paragraph("MOHAMED RAMADAN (ELNEMER)", t_style),
    Paragraph("Full-Stack Python & AI Developer | Software Engineer", sub_style),
    Paragraph("Alexandria, Egypt &nbsp;|&nbsp; <a href='mailto:Elnemer.dev@gmail.com'><font color='#2b6cb0'><u>Elnemer.dev@gmail.com</u></font></a> &nbsp;|&nbsp; +201212968241 &nbsp;|&nbsp; <a href='https://github.com/M-Elnemer-dev'><font color='#2b6cb0'><u>github.com/M-Elnemer-dev</u></font></a> &nbsp;|&nbsp; <a href='https://www.linkedin.com/in/mohamed-elnemer-061093427'><font color='#2b6cb0'><u>linkedin.com/in/mohamed-elnemer</u></font></a>", c_style),
    
    Paragraph("EXECUTIVE SUMMARY", sec_style),
    Paragraph("Results-driven Software Engineer and AI Training Specialist focused on Python development, LLM API integration, and AI code evaluation. Proficient in Python 3.13, JavaScript, RESTful APIs, dialogue state management, and code benchmarking. Proven expertise in evaluating, debugging, and refactoring AI-generated code for algorithmic efficiency, edge-case resilience, and security vulnerability analysis.", b_style),
    
    Paragraph("TECHNICAL STACK & CORE COMPETENCIES", sec_style),
    Paragraph("• <b>Languages & Core:</b> Python 3.13, JavaScript (ES6+), HTML5, CSS3, Data Structures & Algorithms, Asyncio.", b_style),
    Paragraph("• <b>AI & LLM Engineering:</b> LLM Integration (OpenAI API / g4f), Prompt Engineering, Code Benchmarking, Automated Text Analysis.", b_style),
    Paragraph("• <b>Bot & Web Engineering:</b> Telegram Bot API, Webhooks, Conversational Flows, Dialogue State Management, RESTful APIs.", b_style),
    Paragraph("• <b>Testing, Security & Quality:</b> AI Code Evaluation & Refactoring, Vulnerability Analysis, Debugging, Unit Testing, Code Review.", b_style),
    Paragraph("• <b>Cloud & DevOps:</b> Git, GitHub, Linux / Termux, Cloud Hosting (Railway, PaaS), Environment Configs (.env).", b_style),
    
    Paragraph("PRACTICAL EXPERIENCE", sec_style),
    Paragraph("<b>Freelance Software Engineer & AI Code Evaluator</b> <font color='#718096' size=8><b>(2024 – Present)</b></font>", b_style),
    Paragraph("• Evaluated, benchmarked, and refactored 100+ AI-generated Python scripts for correctness, execution efficiency, memory usage, and security vulnerabilities.", b_style),
    Paragraph("• Conducted system vulnerability assessments, code audits, and static code analysis to enforce clean architecture and zero-silent-failure standards.", b_style),
    Paragraph("• Designed, tested, and deployed production-grade messaging bots and web integration backends with comprehensive error recovery protocols.", b_style),
    
    Paragraph("FEATURED PORTFOLIO PROJECTS", sec_style),
    Paragraph("<b>1. AI Conversational Assistant Bot</b>", b_style),
    Paragraph("<i>Repository: <a href='https://github.com/M-Elnemer-dev/ai-telegram-bot'><font color='#2b6cb0'><u>github.com/M-Elnemer-dev/ai-telegram-bot</u></font></a> &nbsp;|&nbsp; Live Demo: <a href='https://t.me/MyMohamedAssistant_bot'><font color='#2b6cb0'><u>t.me/MyMohamedAssistant_bot</u></font></a></i>", b_style),
    Paragraph("<b>Tech Stack:</b> Python 3.13, python-telegram-bot, LLM APIs (g4f), Termux/Linux, Railway", b_style),
    Paragraph("• Engineered a 24/7 interactive Telegram assistant capable of parsing natural language and executing complex contextual prompts.", b_style),
    Paragraph("• Implemented robust fallback logic, async task handling, and exception management to eliminate downtime and unhandled exceptions.", b_style),
    Paragraph("• Managed complete Git lifecycle, environment variable security, and automated continuous deployment pipeline.", b_style),
    
    Paragraph("<b>2. Multi-Format AI Summarizer & Document Bot</b>", b_style),
    Paragraph("<i>Repository: <a href='https://github.com/M-Elnemer-dev/ai-telegram-bot-2'><font color='#2b6cb0'><u>github.com/M-Elnemer-dev/ai-telegram-bot-2</u></font></a> &nbsp;|&nbsp; Live Demo: <a href='https://t.me/ElnemerAssistant_bot'><font color='#2b6cb0'><u>t.me/ElnemerAssistant_bot</u></font></a></i>", b_style),
    Paragraph("<b>Tech Stack:</b> Python 3.13, python-telegram-bot, LLM Integration, File Parsers (PDF, Word)", b_style),
    Paragraph("• Built a bilingual (Arabic & English) bot processing raw text and parsing PDF/Word documents for instant AI summarization.", b_style),
    Paragraph("• Structured output responses with custom prompt templates for highly accurate, concise, and bulleted analytical summaries.", b_style),
    Paragraph("• Handled multi-turn dialogue user states, strict input validation, and platform-specific message formatting.", b_style),
    
    Paragraph("EDUCATION", sec_style),
    Paragraph("<b>Faculty of Law — Alexandria University, Egypt</b> <font color='#718096' size=8><b>(Expected Graduation: 2030)</b></font>", b_style),
    Paragraph("Flexible external program enabling full-time focus and immediate availability for software engineering projects and remote AI training roles.", b_style),
    
    Paragraph("LANGUAGES", sec_style),
    Paragraph("• <b>English:</b> Upper-Intermediate (B2) &nbsp;&nbsp;|&nbsp;&nbsp; • <b>Arabic:</b> Native", b_style)
]

doc.build(story)
print("\n[+] Done! CV with exact LinkedIn link generated in Downloads.\n")
