# wireframed
A bookmarklet that strips styles down to the least polished look possible (Comic Sans included).

## Building
(compile.py) is a script that converts the context of (bookmarklet.js) into a bookmarklet. It should support a plain install of Python 2.7+ and 3.0+. Run as below:

`$ python compile.py`

## Usage
Add the contents of compiled.js as a bookmark to your toolbar. Find a website, and click it!

...or just drag this to your toolbar: [Get it wireframed!](javascript: %28%0A%20%20%20%20function%28%29%20%7B%0A%20%20%20%20%20%20%20%20var%20styleCSS%3D%22%2A%7Bbackground%3Argba%280%2C0%2C0%2C0.02%29%21important%3Bcolor%3Ablack%21important%3Bfont-family%3A%27Comic%20Sans%20MS%27%2CArial%21important%3Bfont-size%3A110%25%3Bpadding%3A2px%7Dinput%2Ctextarea%2Cselect%2Cbutton%2Ca%7Bborder%3A1px%20dashed%20black%21important%3Bpadding%3A2px%3B%7Dbody%2Chtml%2Cdiv%7Bpadding%3A0%3Bmargin%3A0%3B%7D%22%3B%0A%20%20%20%20%20%20%20%20var%20styleNode%3Ddocument.createElement%28%22style%22%29%3B%0A%20%20%20%20%20%20%20%20styleNode.innerText%3DstyleCSS%3B%0A%20%20%20%20%20%20%20%20document.head.appendChild%28styleNode%29%3B%0A%20%20%20%20%7D%0A%29%28%29%0A%0A)

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History
Created approx 2014 - to fill the need of putting "designs" on paper when using external components with existing UIs.

## Credits
* James Cheese

## License
MIT - [See LICENSE](LICENSE)
