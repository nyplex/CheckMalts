const path = require("path")
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CompressionPlugin = require("compression-webpack-plugin");
const webpack = require("webpack");



module.exports = {
    entry: { //add js file for each django app here
        main: './static/js/index.js',
        home: './home/static/home/js/index.js',
        menu: './menu/static/menu/js/index.js',
        order: './order/static/order/js/index.js',
        stripe: './checkout/static/js/stripe_elements.js',
        checkout_detail: './checkout/static/js/index.js'
    },
    optimization: {
      usedExports: true, // <- remove unused function
    },
    mode: "development", //change to production
    output: {
        filename: 'dist/[name].bundle.js',
        path: path.resolve(__dirname, "static/"),
    },
    devtool: 'inline-source-map', //remove on production
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                    },
                      {
                        loader: 'css-loader',
                        options: {importLoaders: 2, url: false},
                    },
                      {
                        loader: 'postcss-loader',
                        options: {
                          postcssOptions: {
                            config: path.resolve(__dirname, 'postcss.config.js'),
                          },
                        },
                    },
                ],
            },
        ],
    },
    plugins: [
        new MiniCssExtractPlugin({
          filename: "dist/bundle.css",
        }),
        new webpack.ProvidePlugin({
          $: 'jquery',
          jQuery: 'jquery',
        }),
        new CompressionPlugin(),
    ],
}