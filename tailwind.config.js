module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        pink: "#F72585",
        darkpink: "#B5179E",
        purple: "#7209B7",
        darkpurple: "#560BAD",
        trypanblue: "#480CA8",
        darktrypanblue: "#3A0CA3",
        persianblue: "#3F37C9",
        ultramarineblue: "#493AD0",
        dodgerblue: "#4895EF",
        darkyellow: "#D9F9A5",
      },
      spacing: {
        '108': '27rem',
        '120': '30rem',
        '132': '33rem',
        '144': '36rem',
        '156': '39rem',
        '168': '42rem',
        '180': '45rem',
        '192': '48rem'
      }
    },
    fontFamily: {
      bruno: ['Bruno', 'serif'],
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
