#!/bin/bash

# Compile all CMH sections into a single document
# Usage: ./compile.sh

OUTPUT_DIR="../cmh-compiled"
OUTPUT_FILE="$OUTPUT_DIR/cmh-full.md"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Create the full document
cat > "$OUTPUT_FILE" << 'EOF'
# Coherence-Mediated Human Coupling Hypothesis (CMH)
## A Framework for Planetary-Scale Biological Resonance

**Authors:** [To be added]  
**Date:** [To be added]  
**Version:** 1.0

---

EOF

# Append all sections in order
cat 01-abstract.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 02-introduction.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 03-motivation-and-context.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 04-core-hypothesis-statement.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 05-mathematical-framing.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 06-biological-mechanism-candidate.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 07-earth-moon-system.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 08-entanglement-like-behavior.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 09-predictions.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 10-experimental-roadmap.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 11-technological-implications.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 12-philosophical-significance.md >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat 13-conclusion.md >> "$OUTPUT_FILE"

echo "✅ Compiled full document: $OUTPUT_FILE"
echo "📄 Total sections: 13"

