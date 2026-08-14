/**
 * Acxiom Design Tokens — Tailwind preset
 * Source: AcxiomMasterTemplate_2026.pdf (v1.0, January 2026)
 * Companion to design-system/tokens/tokens.json
 *
 * Usage:
 *   // tailwind.config.js
 *   module.exports = {
 *     presets: [require('./design-system/tokens/tailwind.preset.js')],
 *     content: ['./src/**\/*.{html,js,jsx,ts,tsx}'],
 *   }
 */

const acxiom = {
  black: '#000000',
  bone: '#EDECE8',
  white: '#FFFFFF',
  plum: '#2A182E',
  magenta: '#FF00A9',
  blue: '#1A12F7',
  orange: '#FF672D',
  grey: '#C6C6C3',
  'grey-dark': '#A0A0A0',
  'bone-shade': '#D8D6D0',
  cyan: '#00E1FD',
  violet: '#940BE0',
}

module.exports = {
  theme: {
    extend: {
      colors: {
        acxiom,
        // Semantic aliases
        surface: {
          dark: acxiom.black,
          'dark-alt': acxiom.plum,
          light: acxiom.bone,
          'light-alt': acxiom.white,
        },
        // Chart series, in the order the template uses them
        chart: {
          1: acxiom.blue,
          2: acxiom.magenta,
          3: acxiom.plum,
          4: acxiom.grey,
        },
      },

      fontFamily: {
        display: ['Tw Cen MT', 'Twentieth Century', 'Futura', 'Century Gothic', 'Questrial', 'sans-serif'],
        mono: ['Consolas', 'Cascadia Mono', 'SF Mono', 'Menlo', 'monospace'],
      },

      // [size, { lineHeight, letterSpacing }] — pt on the 960x540 slide maps 1:1 to px
      fontSize: {
        display: ['72px', { lineHeight: '1.05', letterSpacing: '0em' }],
        title: ['32px', { lineHeight: '1.15', letterSpacing: '0em' }],
        heading: ['28px', { lineHeight: '1.1', letterSpacing: '0em' }],
        lead: ['16px', { lineHeight: '1.5', letterSpacing: '0em' }],
        body: ['14px', { lineHeight: '1.45', letterSpacing: '0em' }],
        'body-sm': ['12px', { lineHeight: '1.4', letterSpacing: '0em' }],
        caption: ['10px', { lineHeight: '1.3', letterSpacing: '0.05em' }],
        eyebrow: ['11px', { lineHeight: '1.4', letterSpacing: '0.25em' }],
        label: ['8px', { lineHeight: '1.4', letterSpacing: '0.35em' }],
        'footer-line': ['10px', { lineHeight: '1.4', letterSpacing: '0.15em' }],
      },

      letterSpacing: {
        eyebrow: '0.25em',
        label: '0.35em',
        'footer-line': '0.15em',
      },

      spacing: {
        margin: '28.8px', // the 0.4in slide margin
        1: '4px',
        2: '8px',
        3: '12px',
        4: '16px',
        5: '24px',
        6: '28.8px',
        7: '32px',
        8: '48px',
        9: '64px',
      },

      backgroundImage: {
        // The signature cover treatment
        glow: 'linear-gradient(75deg, #000000 0%, #2A182E 35%, #940BE0 70%, #FF00A9 100%)',
        'cyan-magenta': 'linear-gradient(180deg, #00E1FD 0%, #FF00A9 100%)',
        'magenta-violet': 'linear-gradient(180deg, #FF00A9 0%, #940BE0 100%)',
        'orange-violet': 'linear-gradient(180deg, #FF672D 0%, #940BE0 100%)',
      },

      borderRadius: {
        // Flow-chart boxes are square-cornered; radius is the exception
        none: '0',
        pill: '999px',
      },

      borderWidth: {
        hairline: '0.75px',
        thick: '2px',
      },

      aspectRatio: {
        slide: '16 / 9',
      },

      maxWidth: {
        canvas: '960px',
      },
    },
  },
}
