function showSection(section){
    if (section == 'insert'){
        document.getElementById('browse').style.display = 'none';
        document.getElementById('create').style.display ='block';
        document.getElementById('update').style.display = 'none';
        document.getElementById('delete').style.display = 'none';

    }
    else if (section == 'update'){
        document.getElementById('browse').style.display = 'none';
        document.getElementById('create').style.display ='none';
        document.getElementById('update').style.display = 'block';
        document.getElementById('delete').style.display = 'none';

    }
    else if (section == 'all'){
        document.getElementById('browse').style.display = 'table';
        document.getElementById('create').style.display ='block';
        document.getElementById('update').style.display = 'block';
        document.getElementById('delete').style.display = 'block';
        document.getElementById('hide').style.display = 'block';
        document.getElementById('all').style.display = 'none';
    }
    else if (section == 'cancel'){
        document.getElementById('browse').style.display = 'table';
        document.getElementById('create').style.display ='none';
        document.getElementById('update').style.display = 'none';
        document.getElementById('delete').style.display = 'none';

    }
    else if (section =='delete'){
        document.getElementById('browse').style.display = 'none';
        document.getElementById('create').style.display ='none';
        document.getElementById('update').style.display = 'none';
        document.getElementById('delete').style.display = 'block'; 
    }
    else if (section =='hide'){
        document.getElementById('browse').style.display = 'table';
        document.getElementById('create').style.display = 'none';
        document.getElementById('update').style.display = 'none';
        document.getElementById('delete').style.display = 'none';
        document.getElementById('hide').style.display = 'none';
        document.getElementById('all').style.display = 'block';
    }
}

function newOrder() {showSection('insert');}
function updateOrder() {showSection('update');}
function showAll() {showSection('all');}
function hideAll() {showSection('hide');}
function cancelOrder() {showSection('cancel');}
function deleteOrder() {showSection('delete');}