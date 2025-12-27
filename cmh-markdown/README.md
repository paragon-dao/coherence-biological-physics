# CMH Markdown Sections

This folder contains cleaned, formatted Markdown versions of all CMH sections, ready for compilation into various publication formats.

## File Structure

### Core Document Sections (13 files)
1. `01-abstract.md` - Abstract
2. `02-introduction.md` - Introduction
3. `03-motivation-and-context.md` - Motivation and Context
4. `04-core-hypothesis-statement.md` - Core Hypothesis Statement
5. `05-mathematical-framing.md` - Mathematical Framing (with LaTeX math)
6. `06-biological-mechanism-candidate.md` - Biological Mechanism Candidate
7. `07-earth-moon-system.md` - Earth-Moon System as Resonant Mediator
8. `08-entanglement-like-behavior.md` - Entanglement-Like Behavior Definition
9. `09-predictions.md` - Predictions and Testable Consequences
10. `10-experimental-roadmap.md` - Experimental Roadmap
11. `11-technological-implications.md` - Technological Implications
12. `12-philosophical-significance.md` - Philosophical and Scientific Significance
13. `13-conclusion.md` - Conclusion

## Formatting Features

- ✅ Proper Markdown headers (`#`, `##`, `###`)
- ✅ LaTeX math equations (`$...$` for inline, `$$...$$` for block)
- ✅ Formatted lists (bullets and numbered)
- ✅ Bold text for emphasis
- ✅ Clean structure (removed extra blank lines)
- ✅ Preserved original content (no rewriting)

## Next Steps

1. **Compile full document** - Combine all sections into `cmh-full.md`
2. **Generate HTML** - Convert to HTML with MathJax for equations
3. **Generate PDF** - Convert to LaTeX/PDF for academic submission
4. **Create EPUB** - Convert to book format

## Compilation

To compile all sections into a single document:

```bash
# Using cat (simple)
cat 01-abstract.md 02-introduction.md ... 13-conclusion.md > ../cmh-compiled/cmh-full.md

# Or use the provided compile script
./compile.sh
```

## Source

Original text preserved from `../cmh-sections/` (which were extracted from `../material.txt`)





