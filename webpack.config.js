////////////////////////////////////////////////////////////////////////////////
/*                        Developer(s): Riley Conrardy                        */
////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////
/*                            NPM: Webpack Exports                            */
////////////////////////////////////////////////////////////////////////////////

const path = require('path');
let export_list = [];

export_list.push(
  {
    entry: `./quickstart/@react/quickstart.jsx`,
    output: {
      path: path.join(__dirname, '/quickstart/static/js/'),
      filename:  'quickstart_bundle.js'
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: ['babel-loader']
        }
      ]
    },
    resolve: {
      extensions: ['*', '.js', '.jsx']
    },
  }
);

module.exports = export_list;
