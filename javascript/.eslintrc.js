module.exports = {
  env: {
    browser: true,
    node: true,
  },
  extends: "eslint:recommended",
  rules: {
    indent: [
      "error",
      2,
      {
        ObjectExpression: "first",
      },
    ],
    "linebreak-style": ["error", "unix"],
    "no-console": "off",
    quotes: ["error", "single"],
    semi: ["error", "always"],
  },
};
