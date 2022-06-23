/* UI Controller ***************************/
var UIController = (function() {
    
    //strings used to access the DOM
    var DOMstrings = {
        submitBtn: '.submit-btn',
        firstName: '.first-name-input',
        lastName: '.last-name-input',
        idInput: '.id-input',
        login: '.login',
        problemPage1: '.problem-page1',
        probBtn1: 'prob-btn-1',
        ques1input: 'ques-1-input',
        ques2input: 'ques-2-input',
        ques3input: 'ques-3-input',
        ques4input: 'ques-4-input',
        problemPage2: '.problem-page2',
        probBtn2: 'prob-btn-2',
        problemPage3: '.problem-page3',
        problemPage4: '.problem-page4',
        answerInput: 'answer-input',
        popup: '.popup',
        finalBtn: 'final-btn',
        VsSummary: 'Vs-summary',
        R1Summary: 'R1-summary',
        R2Summary: 'R2-summary',
        R3Summary: 'R3-summary',
        mostInput: 'most-input',
        leastInput: 'least-input',
        lastBtn: 'last-btn',
        response: '.response',
        probDisplay4: '.display-4',
        raw_response: 'text'
    };
    
    return {
        getDOMstrings: function() {
            return DOMstrings;
        }
    }
    
})();

/* GLOBAL Controller *************************/

var controller = (function(UICtrl) {
    
    //get DOM strings so we can use them
    var DOMstr = UICtrl.getDOMstrings();
    
    //set variables for duration timers
    var elapsed = 0.0;
    
    var globalCurrentTime;
    var globalPreviousTime = new Date().getTime();
    var globalTime;
  
    //user object that will be used to store user information
    var user = {
        globalPath: [],
        globalDuration: [],
        numPopups: 0
    }
    
    //setup all event listeners in the program
    var setupEventListeners = function() {
        
        //equation buttons
        var buttonIds = ['eqn', 'equals', 'multiplied', 'divided', 'squared', 'greater', 'less', 'voltage', 'current', 'power'];
        for(var i = 0; i < buttonIds.length; i++) {
            document.getElementById(buttonIds[i]).addEventListener('click', function(event) {
                equationAddWord(event);
                event.preventDefault();
            });
        };
       
    };
    
    //keypress event listener for the popup
    var setupKeypressEventListener = function() {
        var time = 30000;   //30 seconds
            
        var popupTimer = setTimeout(popup, time);

         document.addEventListener('keypress', function(event) {
            //clear timeout
             clearTimeout(popupTimer);
             //reset timer
             popupTimer = setTimeout(popup, time);
             //change visibility of popup back to 0
             document.querySelector(DOMstr.popup).style.visibility = 'hidden';
             document.querySelector(DOMstr.popup).style.opacity = '0';
             
        });
        //equation buttons
        var buttonIds = ['eqn', 'equals', 'multiplied', 'divided', 'squared', 'greater', 'less', 'voltage', 'current', 'power'];
        for(var i = 0; i < buttonIds.length; i++) {
            document.getElementById(buttonIds[i]).addEventListener('click', function(event) {
                //clear timeout
                 clearTimeout(popupTimer);
                 //reset timer
                 popupTimer = setTimeout(popup, time);
                 //change visibility of popup back to 0
                 document.querySelector(DOMstr.popup).style.visibility = 'hidden';
                 document.querySelector(DOMstr.popup).style.opacity = '0';
                event.preventDefault();
            });
        };
    }
    
    var equationAddWord = function(buttonEl) {
        console.log("Entered equationAddword")
        var button  = buttonEl.target;
        var word = button.textContent;     //get word that user clicked on
        
        var textarea = document.getElementById(DOMstr.answerInput);     //select textarea to put words in
        
        //IE support
        if (document.selection) {
            textarea.focus();
            sel = document.selection.createRange();
            sel.text = word;
        }
        //MOZILLA and others
        else if (textarea.selectionStart || textarea.selectionStart == '0') {
            var startPos = textarea.selectionStart;     //get start and end position
            var endPos = textarea.selectionEnd;
            textarea.value = textarea.value.substring(0, startPos)      //put in word at designated position
                + word
                + textarea.value.substring(endPos, textarea.value.length);
            textarea.selectionStart = startPos + word.length;       //set start and end positions to end of the word
            textarea.selectionEnd = startPos + word.length;
            textarea.focus();           //refocus on textarea so Chrome won't lose cursor position
        } else {
            textarea.value += word;
        }
    };

    var paragraphAddSentence = function(sentenceEl) {
        console.log("ENTERED ADD SENTENCE")
        var sentence = sentenceEl.target;
        var word = sentence.textContent;  // get sentence that user clicked on
        console.log(word)

        let option = window.prompt('Please enter "least" or "most"')

        if (option == "least") {
            var textarea = document.getElementById("id_least_confident");     //select textarea to put words in
        }
        else if (option == "most") {
            var textarea = document.getElementById("id_most_confident");     //select textarea to put words in
        }

        console.log(textarea)
        //IE support
        if (document.selection) {
            console.log("IF")
            textarea.focus();
            sel = document.selection.createRange();
            sel.text = word;
        }
        //MOZILLA and others
        else if (textarea.selectionStart || textarea.selectionStart == '0') {
            console.log("ELIF")
            var startPos = textarea.selectionStart;     //get start and end position
            var endPos = textarea.selectionEnd;
            textarea.value = textarea.value.substring(0, startPos)      //put in word at designated position
                + word
                + textarea.value.substring(endPos, textarea.value.length);
            textarea.selectionStart = startPos + word.length;       //set start and end positions to end of the word
            textarea.selectionEnd = startPos + word.length;
            textarea.focus();           //refocus on textarea so Chrome won't lose cursor position
        } else {
            console.log("ELSE")
            textarea.value += word;
        }
    };
    
    var popup = function() {
        document.querySelector(DOMstr.popup).style.visibility = 'visible';
        document.querySelector(DOMstr.popup).style.opacity = '1';
        user.numPopups = user.numPopups + 1;
    }
    
    var delay = function(amt) {
        var start = new Date().getTime();
        while(new Date().getTime() < start + amt);
    };
    
    var endPage = function() {
        document.querySelector(DOMstr.probDisplay4).innerHTML = '<p><em><b>Thank you!</b></em></p>';
     //   document.getElementById(DOMstr.lastBtn).style.display = 'none';
     //   document.getElementById(DOMstr.lastBtn).insertAdjacentHTML('afterend', '<p><em><b>Thank you!</b></em></p>');
    }
    
    window.onload = (event) => {
        if (document.getElementById('page-4')) {
            if (document.getElementById('sentences')) {
                // var paragraph = document.getElementById('sentences').textContent;
                var paragraph = document.getElementsByClassName('sentences');
                // var sentences = paragraph.match( /[^\.!\?]+[\.!\?]+/g);
                console.log("Sentences");
                for (var i = 0; i < paragraph.length; i++) {
                    console.log(paragraph[i].textContent);
                    (function(index) {
                        paragraph[index].addEventListener('click', function(event) {
                            console.log("CLICKED,", index)
                            // paragraph[index].innerHTML = "I AM REBORN"
                            paragraphAddSentence(event)
                            event.preventDefault();
                        })
                    })(i);
                }
                // console.log(sentences)
            }
            else {
                var buttons = document.getElementsByClassName('eqn-btn')
                console.log("Buttons");
                console.log(buttons)
                for (var i = 0; i < buttons.length; i++) {
                    (function(index) {
                        document.getElementById(buttons[index]).addEventListener('click', function(event) {
                            console.log("CLICKED,", index)
                            // paragraph[index].innerHTML = "I AM REBORN"
                            paragraphAddSentence(event)
                            event.preventDefault();
                        })
                    })(i);
                }
            }
        }
    };
    
    return {
        initialize: function() {
            console.log('Application started!');
            var raw_answer = document.getElementById(DOMstr.answerInput);
            console.log(raw_answer);
            console.log("Jo");
            if (document.getElementById('page-2')) {
                setupEventListeners(); 
            }
        }
        
    }
    
})(UIController);

controller.initialize();
