#!/bin/bash

# Create professional HTML from Pandoc output
# This script extracts body content and wraps it in professional styling

INPUT="cmh-full-temp.html"
OUTPUT="cmh-full.html"
BODY_CONTENT="cmh-body-only.html"

# Extract body content (everything between <body> and </body>)
sed -n '/<body>/,/<\/body>/p' "$INPUT" | sed 's/<\/body>.*//' | sed 's/<body>//' > "$BODY_CONTENT"

# Create the professional HTML file
cat > "$OUTPUT" << 'HTMLHEAD'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <meta name="description" content="Coherence-Mediated Human Coupling Hypothesis (CMH) - A Framework for Planetary-Scale Biological Resonance" />
  <title>Coherence-Mediated Human Coupling Hypothesis (CMH)</title>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js" type="text/javascript"></script>
  <script>
    MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']]
      }
    };
  </script>
  <style>
HTMLHEAD

# Now append the professional CSS
cat >> "$OUTPUT" << 'CSSEND'
    /* Professional Academic Document Styling */
    /* Inspired by Nature, Science, and high-quality scientific publications */
    
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    
    html {
      font-size: 16px;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      scroll-behavior: smooth;
    }
    
    body {
      font-family: 'Georgia', 'Times New Roman', 'Times', serif;
      line-height: 1.7;
      color: #1a1a1a;
      background-color: #ffffff;
      max-width: 900px;
      margin: 0 auto;
      padding: 2rem 3rem;
      text-rendering: optimizeLegibility;
      font-kerning: normal;
      hyphens: auto;
      overflow-wrap: break-word;
    }
    
    /* Iframe-friendly: remove margins when in iframe */
    @media (max-width: 1000px) {
      body {
        padding: 1.5rem 2rem;
      }
    }
    
    /* Typography */
    h1 {
      font-size: 2.2rem;
      font-weight: 700;
      line-height: 1.2;
      margin-top: 2.5rem;
      margin-bottom: 1.5rem;
      color: #0a0a0a;
      border-bottom: 3px solid #2563eb;
      padding-bottom: 0.5rem;
    }
    
    h2 {
      font-size: 1.75rem;
      font-weight: 600;
      line-height: 1.3;
      margin-top: 2rem;
      margin-bottom: 1rem;
      color: #1e293b;
    }
    
    h3 {
      font-size: 1.4rem;
      font-weight: 600;
      line-height: 1.4;
      margin-top: 1.75rem;
      margin-bottom: 0.75rem;
      color: #334155;
    }
    
    h4 {
      font-size: 1.2rem;
      font-weight: 600;
      margin-top: 1.5rem;
      margin-bottom: 0.5rem;
      color: #475569;
    }
    
    p {
      margin: 1.2rem 0;
      text-align: justify;
      text-justify: inter-word;
    }
    
    /* Strong emphasis */
    strong {
      font-weight: 700;
      color: #0f172a;
    }
    
    /* Lists */
    ul, ol {
      margin: 1.2rem 0;
      padding-left: 2rem;
    }
    
    li {
      margin: 0.5rem 0;
      line-height: 1.6;
    }
    
    /* Links */
    a {
      color: #2563eb;
      text-decoration: none;
      border-bottom: 1px solid transparent;
      transition: border-color 0.2s;
    }
    
    a:hover {
      border-bottom-color: #2563eb;
    }
    
    a:visited {
      color: #7c3aed;
    }
    
    /* Horizontal rules */
    hr {
      border: none;
      border-top: 2px solid #e2e8f0;
      margin: 2.5rem 0;
    }
    
    /* Table of Contents */
    #TOC {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 1.5rem 2rem;
      margin: 2rem 0 3rem 0;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    #TOC > ul {
      list-style: none;
      padding-left: 0;
    }
    
    #TOC ul {
      list-style: none;
      padding-left: 1.5rem;
      margin-top: 0.5rem;
    }
    
    #TOC li {
      margin: 0.4rem 0;
    }
    
    #TOC a {
      color: #475569;
      font-size: 0.95rem;
      line-height: 1.5;
    }
    
    #TOC a:hover {
      color: #2563eb;
      border-bottom-color: #2563eb;
    }
    
    /* Math equations */
    .MathJax {
      font-size: 1.1em;
    }
    
    /* Code blocks */
    code {
      font-family: 'Courier New', 'Monaco', 'Consolas', monospace;
      font-size: 0.9em;
      background: #f1f5f9;
      padding: 0.2em 0.4em;
      border-radius: 3px;
      color: #1e293b;
    }
    
    pre {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 1rem;
      overflow-x: auto;
      margin: 1.5rem 0;
    }
    
    pre code {
      background: transparent;
      padding: 0;
    }
    
    /* Images and Figures */
    figure {
      margin: 2.5rem auto;
      text-align: center;
      max-width: 100%;
    }
    
    img {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    figcaption {
      margin-top: 1rem;
      font-style: italic;
      color: #64748b;
      font-size: 0.95em;
      text-align: center;
    }
    
    /* Image captions (italic text after images) */
    p:has(+ em), em:first-of-type {
      display: block;
      text-align: center;
      font-style: italic;
      color: #64748b;
      margin-top: -1.5rem;
      margin-bottom: 2rem;
      font-size: 0.95em;
    }
    
    /* Blockquotes */
    blockquote {
      border-left: 4px solid #2563eb;
      padding-left: 1.5rem;
      margin: 1.5rem 0;
      color: #475569;
      font-style: italic;
    }
    
    /* Tables */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      font-size: 0.95em;
    }
    
    th, td {
      padding: 0.75rem;
      text-align: left;
      border-bottom: 1px solid #e2e8f0;
    }
    
    th {
      background: #f8fafc;
      font-weight: 600;
      color: #1e293b;
    }
    
    /* Print styles */
    @media print {
      body {
        max-width: 100%;
        padding: 1rem;
        font-size: 12pt;
        line-height: 1.6;
      }
      
      h1, h2, h3 {
        page-break-after: avoid;
      }
      
      p, h2, h3 {
        orphans: 3;
        widows: 3;
      }
      
      #TOC {
        page-break-after: always;
      }
      
      a {
        color: #000;
        text-decoration: underline;
      }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
      body {
        padding: 1rem 1.5rem;
        font-size: 0.95rem;
      }
      
      h1 {
        font-size: 1.8rem;
      }
      
      h2 {
        font-size: 1.5rem;
      }
      
      h3 {
        font-size: 1.25rem;
      }
      
      #TOC {
        padding: 1rem 1.5rem;
      }
    }
    
    /* Smooth scrolling for anchor links */
    html {
      scroll-padding-top: 2rem;
    }
    
    /* Section spacing */
    section {
      margin: 2rem 0;
    }
    
    /* Abstract styling */
    #abstract {
      background: #f8fafc;
      border-left: 4px solid #2563eb;
      padding: 1.5rem 2rem;
      margin: 2rem 0;
      font-style: italic;
    }
    
    /* Header styling */
    header {
      text-align: center;
      margin-bottom: 3rem;
      padding-bottom: 2rem;
      border-bottom: 2px solid #e2e8f0;
    }
    
    header h1 {
      border-bottom: none;
      margin-bottom: 0.5rem;
    }
    
    header h2 {
      font-size: 1.3rem;
      font-weight: 400;
      color: #64748b;
      margin-top: 0.5rem;
    }
  </style>
</head>
<body>
CSSEND

# Append the body content
cat "$BODY_CONTENT" >> "$OUTPUT"

# Close HTML
echo "</body>" >> "$OUTPUT"
echo "</html>" >> "$OUTPUT"

echo "✅ Created professional HTML: $OUTPUT"

