const {
    defineConfig,
} = require("eslint/config");

const globals = require("globals");
const js = require("@eslint/js");

const {
    FlatCompat,
} = require("@eslint/eslintrc");

const compat = new FlatCompat({
    baseDirectory: __dirname,
    recommendedConfig: js.configs.recommended,
    allConfig: js.configs.all
});

module.exports = defineConfig([{
    languageOptions: {
        globals: {
            ...globals.browser,
            ...globals.node,
        },
    },

    extends: "eslint:recommended",

    rules: {
        indent: ["error", 2, {
            ObjectExpression: "first",
        }],

        "linebreak-style": ["error", "unix"],
        "no-console": "off",
        quotes: ["error", "single"],
        semi: ["error", "always"],
    },
}]);
