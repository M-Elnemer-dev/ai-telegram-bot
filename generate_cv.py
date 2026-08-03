from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import os

pdf_path = "/sdcard/Download/Mohamed_Ramadan_Elnemer_CV.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, textColor=colors.HexColor('#1a365d'), alignment=1, spaceAfter=4)
sub_style = ParagraphStyle('Sub', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#2b6cb0'), alignment=1, spaceAfter=4)
contact_style = ParagraphStyle('Contact', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=colors.HexColor('#4a5568'), alignment=1, spaceAfter=10)
sec_style = ParagraphStyle('Sec', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#1a365d'), spaceBefore=8, spaceAfter=4)
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, textColor=colors.HexColor('#2d3748'), spaceAfter=4)

story = [
    Paragraph("MOHAMED RAMADAN (ELNEMER)", title_style),
    Paragraph("Full-Stack Python & AI Developer | Software Engineer", sub_style),
    Paragraph("Alexandria, Egypt | Elnemer.dev@gmail.com | +201212968241 | github.com/M-Elnemer-dev | linkedin.com/in/mohamed-elnemer", contact_style),
    
    Paragraph("EXECUTIVE SUMMARY", sec_style),
    Paragraph("Results-driven Software Engineer and AI Training Specialist focused on Python development, LLM API integration, and AI code evaluation. Proficient in Python 3.13, JavaScript, RESTful APIs, dialogue state management, and code benchmarking. Proven expertise in evaluating, debugging, and refactoring AI-generated code for algorithmic efficiency, edge-case resilience, and security vulnerability analysis.", body_style),
    
    Paragraph("TECHNICAL STACK & CORE COMPETENCIES", sec_style),
    Paragraph("<b>• Languages & Core:</b> Python 3.13, JavaScript (ES6+), HTML5, CSS3, Data Structures & Algorithms, Asyncio.", body_style),
    Paragraph("<b>• AI & LLM Engineering:</b> LLM Integration (OpenAI API / g4f), Prompt Engineering, Code Benchmarking, Automated Text Analysis.", body_style),
    Paragraph("<b>• Bot & Web Engineering:</b> Telegram Bot API, Webhooks, Conversational Flows, Dialogue State Management, RESTful APIs.", body_style),
    Paragraph("<b>• Testing, Security & Quality:</b> AI Code Evaluation & Refactoring, Vulnerability Analysis, Debugging, Unit Testing, Code Review.", body_style),
    Paragraph("<b>• Cloud & DevOps:</b> Git, GitHub, Linux / Termux, Cloud Hosting (Railway, PaaS), Environment Configs (.env).", body_style),
    
    Paragraph("PRACTICAL EXPERIENCE", sec_style),
    Paragraph("<b>Freelance Software Engineer & AI Code Evaluator</b> (2024 – Present)", body_style),
    Paragraph("• Evaluated, benchmarked, and refactored 100+ AI-generated Python scripts for correctness, execution efficiency, memory usage, and security vulnerabilities.", body_style),
    Paragraph("• Conducted system vulnerability assessments, code audits, and static code analysis to enforce clean architecture and zero-silent-failure standards.", body_style),
    Paragraph("• Designed, tested, and deployed production-grade messaging bots and web integration backends with comprehensive error recovery protocols.", body_style),
    
    Paragraph("FEATURED PORTFOLIO PROJECTS", sec_style),
    Paragraph("<b>1. AI Conversational Assistant Bot</b><br/><i>Repository: github.com/M-Elnemer-dev/ai-telegram-bot | Live Demo: t.me/MyMohamedAssistant_bot</i>", body_style),
    Paragraph("• Engineered a 24/7 interactive Telegram assistant capable of parsing natural language and executing complex contextual prompts.", body_style),
    Paragraph("• Implemented robust fallback logic, async task handling, and exception management to eliminate downtime.", body_style),
    
    Paragraph("<b>2. Multi-Format AI Summarizer & Document Bot</b><br/><i>Repository: github.com/M-Elnemer-dev/ai-telegram-bot-2 | Live Demo: t.me/ElnemerAssistant_bot</i>", body_style),
    Paragraph("• Built a bilingual (Arabic & English) bot processing raw text and parsing PDF/Word documents for instant AI summarization.", body_style),
    Paragraph("• Structured output responses with custom prompt templates for highly accurate concise summaries.", body_style),
    
    Paragraph("EDUCATION", sec_style),
    Paragraph("<b>Faculty of Law — Alexandria University, Egypt</b> (Expected Graduation: 2030)<br/>Flexible external program enabling full-time focus and immediate availability for software engineering projects.", body_style),
    
    Paragraph("LANGUAGES", sec_style),
    Paragraph("• <b>English:</b> Upper-Intermediate (B2) | • <b>Arabic:</b> Native", body_style)
]

doc.build(story)
print("\n Done! Check your Downloads folder for: Mohamed_Ramadan_Elnemer_CV.pdf\n")
