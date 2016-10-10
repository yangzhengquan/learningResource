var TableEditable = function () {

    return {

        //main function to initiate the module
        init: function () {
            

           

            var oTable = $('#sample_editable_1').dataTable({
                /*"aLengthMenu": [
                    [5, 15, 20, -1],
                    [5, 15, 20, "All"] // change per page values here
                ],*/
                // set the initial value
               // "iDisplayLength": 15,
                
                //"sPaginationType": "bootstrap",
                /*"oLanguage": {
                    "sLengthMenu": "_MENU_ records",
                    "oPaginate": {
                        "sPrevious": "Prev",
                        "sNext": "Next"
                    }
                },*/
				"paging":   false,
				"ordering": false,
				"info":     false,
				//"order": [[ 3, "desc" ]],
                "aoColumnDefs": [{
                        'bSortable': false,
                        'aTargets': [0,1]
                    }
                ]
            });

            //jQuery('#sample_editable_1_wrapper .dataTables_filter input').addClass("form-control input-medium"); // modify table search input
            //jQuery('#sample_editable_1_wrapper .dataTables_length select').addClass("form-control input-small"); // modify table per page dropdown
            /*jQuery('#sample_editable_1_wrapper .dataTables_length select').select2({
                showSearchInput : false //hide search box with special css class
            }); // initialize select2 dropdown*/

            
           

           
        }

    };

}();