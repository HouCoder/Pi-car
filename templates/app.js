(() => {
    $('.container__icon').on('mousedown', function() {
        const $current = $(this);

        $current.addClass('is-active');
        console.log('mousedown');
    }).on('mouseup', function() {
        const $current = $(this);

        $current.removeClass('is-active');
        console.log('mouseup');
    });
})();
