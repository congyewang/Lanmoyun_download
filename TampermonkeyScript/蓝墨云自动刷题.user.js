// ==UserScript==
// @name         蓝墨云自动刷题
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  蓝墨云自动刷题, 按菜单上的Start开始
// @author       Laurence
// @grant        GM_registerMenuCommand
// @match        https://www.mosoteach.cn/web/index.php?c=interaction_quiz*
// @match        https://www.mosoteach.cn/web/index.php?c=interaction&m=index&clazz_course_id=*
// ==/UserScript==

(function () {
    'use strict';
    // Your code here...
    var url_list = document.getElementsByClassName("interaction-row");
    // 添加按钮
    GM_registerMenuCommand('Start', function () {
        for (let i = 0; i < url_list.length; i++) {
            document.getElementsByClassName("interaction-row")[i].click();
            var answer_list = document.getElementsByTagName("i");
            for (let j = 0; j < answer_list.length; j++) {//j++是针对多选题全选, 单选全A请改为j=j+4, 判断题为j=j+2. j++比较万能, 但是不知道能选出来啥
                answer_list[j].click()
            };
            document.getElementsByClassName("button-routine submit-button")[0].click();
            document.getElementsByClassName("button-routine tips-ok")[0].click();
            document.getElementsByClassName("button-routine tips-ok")[0].click();
        }
    }, 'S');
})();