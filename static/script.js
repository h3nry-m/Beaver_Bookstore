
// Modifies browse and create containers to only show Create operations for a page.
function newOrder() {
    document.getElementById('browse').style.display = 'none';
    document.getElementById('create').style.display ='block';
}
// Modifies browse and create containers to only show the main table for a page.
function cancelOrder() {
    document.getElementById('browse').style.display = 'table';
    document.getElementById('create').style.display ='none';
}
