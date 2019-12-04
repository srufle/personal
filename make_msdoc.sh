#!/bin/bash
docker pull jagregory/pandoc
docker run -v $(pwd):/source jagregory/pandoc -o techs.docx -f html -t docx technologies.html
docker run -v $(pwd):/source jagregory/pandoc -o output_github.docx -f markdown -t docx rufle_stephen_resume.md
echo "Done"

