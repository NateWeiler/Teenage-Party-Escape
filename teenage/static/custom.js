$(document).ready(function() {

            $('.next-scene-click').click(function() {
                $(this).parent().parent().next().removeClass('hidden');
                $(this).parent().parent().hide();
            });