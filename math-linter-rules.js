// math-linter-rules.js
// Custom math block formatting rules for Obsidian via QuickAdd

// Rule definitions - order matters!
const rules = [
  // Phase 1: First identify and normalize complete math blocks
  {
    name: "capture-and-format-math-blocks",
    // Capture entire math block including preceding context
    pattern: /^([ \t]*(?:[-+*] [^\n]*?)?\n?[ \t]*)(\$\$)([\s\S]*?)(\$\$)/gm,
    replacement: function(match, contextAndIndent, openDelim, content, closeDelim) {
      // Check if this is part of a bullet point (preceding line ends with colon)
      const isBulletPoint = /[-+*] [^\n]*?:[ \t]*$/.test(contextAndIndent.split('\n')[0]);
      
      // Determine the base indentation
      let baseIndent = '';
      const indentMatch = contextAndIndent.match(/^([ \t]*)/);
      if (indentMatch) {
        baseIndent = indentMatch[1];
      }
      
      // For bullet points, we need to add 2 spaces of indentation
      const contentIndent = isBulletPoint ? baseIndent + '  ' : baseIndent;
      
      // Remove only the leading and trailing newlines while preserving internal formatting
      const cleanedContent = content
        .replace(/^\s*\n+/, '')     // Remove newlines at the start
        .replace(/\n+\s*$/, '');    // Remove newlines at the end
      
      return `${baseIndent}${openDelim}\n${contentIndent}${cleanedContent}\n${baseIndent}${closeDelim}`;
    }
  },
  
  // Phase 2: Fix specific patterns for bullet point math blocks
  {
    name: "fix-bullet-point-math-blocks",
    pattern: /(^[ \t]*[-+*][^\n]*?:)[ \t]*\n{2,}([ \t]*)(\$\$)/gm,
    replacement: "$1\n$2$3"
  },
  
  // Phase 3: Handle spacing around math blocks
  {
    name: "ensure-blank-line-before-math-block",
    pattern: /([^\n])\n(?!\n)(?![ \t]*[-+*][^\n]*?:[ \t]*\n)([ \t]*\$\$)/g,
    replacement: "$1\n\n$2"
  },
  {
    name: "ensure-blank-line-after-math-block",
    pattern: /(\$\$)\n(?!\n)([^\n])/g,
    replacement: "$1\n\n$2"
  },
  
  // Phase 4: Clean up any excessive whitespace created by the previous rules
  {
    name: "remove-excess-newlines-before-math-block",
    pattern: /\n{3,}([ \t]*\$\$)/g,
    replacement: "\n\n$1"
  },
  {
    name: "remove-excess-newlines-after-math-block",
    pattern: /(\$\$)\n{3,}/g,
    replacement: "$1\n\n"
  },
  {
    name: "normalize-consecutive-newlines",
    // Replace any sequence of 3+ newlines with exactly 2 newlines
    pattern: /\n{3,}/g,
    replacement: "\n\n"
  }
];

// Function that applies all rules
function formatMathBlocks(text) {
  if (typeof text !== 'string') {
    console.error('Input is not a string:', typeof text);
    return text;
  }
  
  let result = text;
  for (const rule of rules) {
    try {
      if (typeof rule.replacement === 'function') {
        result = result.replace(rule.pattern, rule.replacement);
      } else {
        result = result.replace(rule.pattern, rule.replacement);
      }
    } catch (error) {
      console.error(`Error applying rule ${rule.name}:`, error);
    }
  }
  return result;
}

// Main QuickAdd function
module.exports = async (params) => {
  try {
    // Get the current active file
    const activeFile = app.workspace.getActiveFile();
    if (!activeFile) {
      new Notice('No active file found');
      return;
    }
    
    // Read the file content
    const content = await app.vault.read(activeFile);
    
    // Apply the formatting rules
    const formattedContent = formatMathBlocks(content);
    
    // Only modify if changes were made
    if (content !== formattedContent) {
      await app.vault.modify(activeFile, formattedContent);
      new Notice('Math blocks formatted successfully!');
    } else {
      new Notice('No changes needed - math blocks already properly formatted!');
    }
    
  } catch (error) {
    console.error('Error in math formatting script:', error);
    new Notice('Error formatting math blocks: ' + error.message);
  }
};