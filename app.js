window.addEventListener('DOMContentLoaded',()=>{
    const squares=Array.from(document.querySelectorAll('.square'));
    const playerDisplay=document.querySelector('.display-player');
    const resetBtn=document.querySelector('#reset');
    const verdict=document.querySelector('.verdict');

    let board=['','','','','','','','',''];
    /* 
    index des éléments du tableau squares 
        [0] [1] [2]
        [3] [4] [5]
        [6] [7] [8]
    */
    let currentPlayer= 'X';
    let isGameOn=true;

    const PLAYERX_WINNER='PlayerX_Won';
    const PLAYERO_WINNER='PlayerO_Won';
    const TIE='TIE';
   
    //les différentes combinaisons gagnantes possibles
    const winningConditions=[
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ];
    function resultValidation(){
        let roundWon=false;
        //8 index donc on incrémente i jusqu'à 7
        for(let i=0;i<=7;i++){
            const winCondition=winningConditions[i];
            const a=board[winCondition[0]];
            const b=board[winCondition[1]];
            const c=board[winCondition[2]];
            if(a===''||b===''||c===''){
                continue;
            }
            if(a===b && b===c){
                roundWon=true;
                break;
            }
        }
        //si roundWon est true
        if(roundWon){
            //Condition ? Valeur si True : Valeur si False
            announce(currentPlayer==="X" ? PLAYERX_WINNER : PLAYERO_WINNER);
            isGameOn=false;
            return
        }
        if(!board.includes('')){
            announce(TIE);
        }
    }
    const announce=(situation)=>{
        //selon la situation rencontrée, j'applique les instructions correspondantes
        switch(situation){
            //joueur O a gagné
            case PLAYERO_WINNER:
                verdict.innerHTML='Player <span class="playerO">O</span> Won !';
                break;
            //joueur X a gagné
            case PLAYERX_WINNER:
                verdict.innerHTML='Player <span class="playerX">X</span> Won !';
                break;
            //personne n'a gagné
            case TIE:
                verdict.innerText='We have a tie!';
        }
        verdict.classList.remove('hide')
    }
    const isValidAction=(square)=>{
        //l'utilisateur ne peut pas jouer sur une case déjà occupée
        if(square.innerText==="X"||square.innerText==="O"){
            return false;
        }
        return true;
    }
    const updateBoard=(index)=>{
        //j'affecte à la case la lettre du joueur actuel
        board[index]=currentPlayer
    }
    const changePlayer=()=>{
       playerDisplay.classList.remove('player'+currentPlayer);
       currentPlayer=currentPlayer==="X"?"O":"X";
       playerDisplay.innerText=currentPlayer;
       playerDisplay.classList.add('player'+currentPlayer);
    }
    const userAction=(square,index)=>{
        if(isValidAction(square)&&isGameOn){
            square.innerText=currentPlayer;
            square.classList.add('player'+currentPlayer);
            updateBoard(index);
            resultValidation();
            changePlayer();
        }
    }
    squares.forEach((square,index) => {
        square.addEventListener('click',() => {
            userAction(square,index);
        })
    })
    //Fonction de réinitialisation du jeu
    const resetGame=()=>{
        board=['','','','','','','','',''];
        isGameOn=true;
        verdict.classList.add('hide');

        if(currentPlayer==="O"){
            changePlayer();
        }
        squares.forEach(square=>{
            square.innerText='';
            square.classList.remove('playerX');
            square.classList.remove('playerO');
        })
    }
    resetBtn.addEventListener('click',resetGame);
})