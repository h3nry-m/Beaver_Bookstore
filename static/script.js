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
        document.getElementById('browse').style.display = 'block';
        document.getElementById('create').style.display ='block';
        document.getElementById('update').style.display = 'block';
        document.getElementById('delete').style.display = 'block';

    }
    else if (section == 'cancel'){
        document.getElementById('browse').style.display = 'block';
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
}

function newOrder() {showSection('insert');}
function updateOrder() {showSection('update');}
function showAll() {showSection('all');}
function cancelOrder() {showSection('cancel');}
function deleteOrder() {showSection('delete');}