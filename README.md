# Professional LaTeX Resume

A clean, modern resume template using the AltaCV class, customized for robotics and software engineering professionals.

## Features

- Clean, professional design with customizable colors and sections
- Separate sections for Education, Experience, Skills, Research, and Projects
- Support for academic and professional achievements
- Modern icons for contact information
- Optimized layout for technical roles

## Prerequisites

To compile this resume, you'll need:

- A LaTeX distribution (e.g., TeX Live, MiKTeX)
- The following LaTeX packages:
  - altacv
  - geometry
  - fontawesome
  - xcolor
  - tikz
  - and other standard packages

## Usage

1. Clone this repository:
```bash
git clone https://github.com/AndrewGerstenslager/latex_resume.git
```

2. Edit the resume content in `resume.tex`

3. Compile using:
```bash
pdflatex resume.tex
```

## Customization

### Colors
You can modify the colors by adjusting the following in the preamble:
```latex
\definecolor{VividPurple}{HTML}{000000}
\definecolor{SlateGrey}{HTML}{2E2E2E}
\definecolor{LightGrey}{HTML}{2E2E2E}
```

### Sections
The resume is organized into sections using:
```latex
\cvsection{Section Name}
```

### Contact Info
Update your personal information in:
```latex
\personalinfo{%
    \phone{your-phone}
    \homepage{your-website}
    \email{your-email}
    \linkedin{your-linkedin}
    \github{your-github}
}
```

## License

This template is based on AltaCV, which is distributed under the LaTeX Project Public License (LPPL).

## Acknowledgments

- Original AltaCV class by LianTze Lim
- Modified and customized for technical and robotics professionals

