const fs = require('fs');
const path = require('path');

// Math notation standardization rules
const notationRules = [
  // Expected Value standardization
  {
    name: "standardize-expected-value",
    pattern: /\\mathbb\s*\{\s*E\s*\}\s*[\[\(]([^)\]]+)[\]\)]/g,
    replacement: "E($1)"
  },
  {
    name: "standardize-expected-value-no-braces",
    pattern: /\\mathbb\s+E\s*[\[\(]([^)\]]+)[\]\)]/g,
    replacement: "E($1)"
  },
  
  // Variance standardization
  {
    name: "standardize-variance-text",
    pattern: /\\text\s*\{\s*Var\s*\}\s*\(([^)]+)\)/g,
    replacement: "V($1)"
  },
  {
    name: "standardize-variance-mathrm",
    pattern: /\\mathrm\s*\{\s*Var\s*\}\s*\(([^)]+)\)/g,
    replacement: "V($1)"
  },
  {
    name: "standardize-variance-plain",
    pattern: /\bVar\s*\(([^)]+)\)/g,
    replacement: "V($1)"
  },
  {
    name: "standardize-variance-lowercase",
    pattern: /\\text\s*\{\s*var\s*\}\s*\(([^)]+)\)/g,
    replacement: "V($1)"
  },
  
  // Probability standardization
  {
    name: "standardize-probability-mathbb",
    pattern: /\\mathbb\s*\{\s*P\s*\}\s*\(([^)]+)\)/g,
    replacement: "P($1)"
  },
  {
    name: "standardize-probability-mathbb-no-braces",
    pattern: /\\mathbb\s+P\s*\(([^)]+)\)/g,
    replacement: "P($1)"
  },
  {
    name: "standardize-probability-text-pr",
    pattern: /\\text\s*\{\s*Pr\s*\}\s*\(([^)]+)\)/g,
    replacement: "P($1)"
  },
  
  // Covariance standardization
  {
    name: "standardize-covariance-plain",
    pattern: /\bCov\s*\(([^)]+)\)/g,
    replacement: "\\text{Cov}($1)"
  }
];

function standardizeNotation(content) {
  let result = content;
  
  for (const rule of notationRules) {
    result = result.replace(rule.pattern, rule.replacement);
  }
  
  return result;
}

function formatMathBlocks(text) {
  // Pattern to match math blocks with any content between $$, capturing preceding whitespace
  const mathBlockPattern = /(^|\n)(\s*)(\$\$)([\s\S]*?)(\$\$)/g;
  
  return text.replace(mathBlockPattern, (match, lineStart, indent, openDelim, content, closeDelim) => {
    // Remove all leading and trailing whitespace from content
    let cleanedContent = content.replace(/^\s+|\s+$/g, '');
    
    // Apply notation standardization
    cleanedContent = standardizeNotation(cleanedContent);
    
    // If content is empty, return empty math block
    if (!cleanedContent) {
      return `${lineStart}${indent}$$${indent}$$`;
    }
    
    // If there's indentation (we're in a list or quote block), preserve it and use inline format
    if (indent) {
      return `${lineStart}${indent}$$${cleanedContent}$$`;
    }
    
    // Return properly formatted math block without indentation (block format)
    return `${lineStart}$$\n${cleanedContent}\n$$`;
  });
}

function processFile(filePath, fix = false) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    const formatted = formatMathBlocks(content);
    
    if (content !== formatted) {
      console.log(`📝 Issues found in: ${path.basename(filePath)}`);
      
      if (fix) {
        fs.writeFileSync(filePath, formatted, 'utf8');
        console.log(`✅ Fixed: ${path.basename(filePath)}`);
      } else {
        console.log(`   Run with 'node math-linter.js fix' to automatically correct`);
      }
    } else {
      console.log(`✅ ${path.basename(filePath)} - OK`);
    }
  } catch (error) {
    console.error(`❌ Error processing ${filePath}:`, error.message);
  }
}

function findMarkdownFiles(dir, files = []) {
  const items = fs.readdirSync(dir);
  
  for (const item of items) {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);
    
    if (stat.isDirectory() && !item.startsWith('.')) {
      findMarkdownFiles(fullPath, files);
    } else if (item.endsWith('.md')) {
      files.push(fullPath);
    }
  }
  
  return files;
}

// Main execution
const args = process.argv.slice(2);
const fix = args.includes('fix');
const targetFile = args.find(arg => arg.endsWith('.md'));

if (targetFile) {
  console.log(`Processing: ${targetFile}`);
  processFile(targetFile, fix);
} else {
  console.log('🔍 Scanning for Markdown files...\n');
  const files = findMarkdownFiles(process.cwd());
  
  files.forEach(file => {
    processFile(file, fix);
  });
  
  console.log(`\n📊 Processed ${files.length} files`);
}