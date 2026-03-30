var app = new Vue({
    el: '#app',
    data: {
        inStr: ''
    },
    methods: {
        palindrome: function() {
            if (this.inStr.length == 0) return;
            var rStr = this.inStr.split('').reverse().join('');
            if (this.inStr == rStr) {
                return '回文です!';
            } else {
                return '回文ではありません';
            }
        },
        highlightedChars: function() {
            if (this.inStr.length == 0) return [];
            var chars = this.inStr.split('');
            var mismatch = new Array(chars.length).fill(false);
            for (var i = 0; i < Math.floor(chars.length / 2); i++) {
                if (chars[i] !== chars[chars.length - 1 - i]) {
                    mismatch[i] = true;
                    mismatch[chars.length - 1 - i] = true;
                }
            }
            return chars.map(function(c, i) {
                return { char: c, mismatch: mismatch[i] };
            });
        }
    }
});
