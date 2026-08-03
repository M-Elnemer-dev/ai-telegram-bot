from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = "/sdcard/Download/Mohamed_Ramadan_Elnemer_CV.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=40, bottomMargin=40)
styles = getSampleStyleSheet()

t_style = ParagraphStyle('T', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=22, textColor=colors.HexColor('#1a365d'), alignment=1, spaceAfter=6)
sub_style = ParagraphStyle('Sub', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=12, textColor=colors.HexColor('#2b6cb0'), alignment=1, spaceAfter=6)
c_style = ParagraphStyle('C', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, textColor=colors.HexColor('#4a5568'), alignment=1, spaceAfter=15)
sec_style = ParagraphStyle('Sec', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, textColor=colors.HexColor('#1a365d'), spaceBefore=14, spaceAfter=6)
b_style = ParagraphStyle('B', parent=styles['Normal'], fontName='Helvetica', fontSize=10, textColor=colors.HexColor('#2d3748'), leading=14, spaceAfter=5)

story = [
    Paragraph("MOHAMED RAMADAN (ELNEMER)", t_style),
    Paragraph("Full-Stack Python & AI Developer | Software Engineer", sub_style),
    Paragraph("Alexandria, Egypt &nbsp;|&nbsp; Elnemer.dev@gmail.com &nbsp;|&nbsp; +201212968241 &nbsp;|&nbsp; github.com/M-Elnemer-dev &nbsp;|&nbsp; linkedin.com/in/mohamed-elnemer", c_style),
    Spacer(1, 10),
    
    Paragraph("EXECUTIVE SUMMARY", sec_style),
    Paragraph("Results-driven Software Engineer and AI Training Specialist focused on Python development, LLM API integration, and AI code evaluation. Proficient in Python 3.13, JavaScript, RESTful APIs, dialogue state management, and code benchmarking. Proven expertise in evaluating, debugging, and refactoring AI-generated code for algorithmic efficiency, edge-case resilience, and security vulnerability analysis.", b_style),
    Spacer(1, 8),
    
    Paragraph("TECHNICAL STACK & CORE COMPETENCIES", sec_style),
    Paragraph("• <b>Languages & Core:</b> Python 3.13, JavaScript (ES6+), HTML5, CSS3, Data Structures & Algorithms, Asyncio.", b_style),
    Paragraph("• <b>AI & LLM Engineering:</b> LLM Integration (OpenAI API / g4f), Prompt Engineering, Code Benchmarking, Automated Text Analysis.", b_style),
    Paragraph("• <b>Bot & Web Engineering:</b> Telegram Bot API, Webhooks, Conversational Flows, Dialogue State Management, RESTful APIs.", b_style),
    Paragraph("• <b>Testing, Security & Quality:</b> AI Code Evaluation & Refactoring, Vulnerability Analysis, Debugging, Unit Testing, Code Review.", b_style),
    Paragraph("• <b>Cloud & DevOps:</b> Git, GitHub, Linux / Termux, Cloud Hosting (Railway, PaaS), Environment Configs (.env).", b_style),
    Spacer(1, 8),
    
    Paragraph("PRACTICAL EXPERIENCE", sec_style),
    Paragraph("<b>Freelance Software Engineer & AI Code Evaluator</b> <font color='#718096' size=9><b>(2024 – Present)</b></font>", b_style),
    Paragraph("• Evaluated, benchmarked, and refactored 100+ AI-generated Python scripts for correctness, execution efficiency, memory usage, and security vulnerabilities.", b_style),
    Paragraph("• Conducted system vulnerability assessments, code audits, and static code analysis to enforce clean architecture and zero-silent-failure standards.", b_style),
    Paragraph("• Designed, tested, and deployed production-grade messaging bots and web integration backends with comprehensive error recovery protocols.", b_style),
    Spacer(1, 8),
    
    Paragraph("FEATURED PORTFOLIO PROJECTS", sec_style),
    Paragraph("<b>1. AI Conversational Assistant Bot</b>", b_style),
    Paragraph("<i>Repository: github.com/M-Elnemer-dev/ai-telegram-bot &nbsp;|&nbsp; Live Demo: t.me/MyMohamedAssistant_bot</i>", b_style),
    Paragraph("<b>Tech Stack:</b> Python 3.13, python-telegram-bot, LLM APIs (g4f), Termux/Linux, Railway", b_style),
    Paragraph("• Engineered a 24/7 interactive Telegram assistant capable of parsing natural language and executing complex contextual prompts.", b_style),
    Paragraph("• Implemented robust fallback logic, async task handling, and exception management to eliminate downtime and unhandled exceptions.", b_style),
    Paragraph("• Managed complete Git lifecycle, environment variable security, and automated continuous deployment pipeline.", b_style),
    Spacer(1, 6),
    
    Paragraph("<b>2. Multi-Format AI Summarizer & Document Bot</b>", b_style),
    Paragraph("<i>Repository: github.com/M-Elnemer-dev/ai-telegram-bot-2 &nbsp;|&nbsp; Live Demo: t.me/ElnemerAssistant_bot</i>", b_style),
    Paragraph("<b>Tech Stack:</b> Python 3.13, python-telegram-bot, LLM Integration, File Parsers (PDF, Word)", b_style),
    Paragraph("• Built a bilingual (Arabic & English) bot processing raw text and parsing PDF/Word documents for instant AI summarization.", b_style),
    Paragraph("• Structured output responses with custom prompt templates for highly accurate, concise, and bulleted analytical summaries.", b_style),
    Paragraph("• Handled multi-turn dialogue user states, strict input validation, and platform-specific message formatting.", b_style),
    Spacer(1, 8),
    
    Paragraph("EDUCATION", sec_style),
    Paragraph("<b>Faculty of Law — Alexandria University, Egypt</b> <font color='#718096' size=9><b>(Expected Graduation: 2030)</b></font>", b_style),
    Paragraph("Flexible external program enabling full-time focus and immediate availability for software engineering projects and remote AI training roles.", b_style),
    Spacer(1, 8),
    
    Paragraph("LANGUAGES", sec_style),
    Paragraph("• <b>English:</b> Upper-Intermediate (B2) &nbsp;&nbsp;|&nbsp;&nbsp; • <b>Arabic:</b> Native", b_style)
]

doc.build(story)
print("\n[+] 2-Page CV generated in Downloads: Mohamed_Ramadan_Elnemer_CV.pdf\n")
