/* global $ */
$( document ).ready( function () {

    /**
     *
     * Initialize fullpage.js
     *
     */

    $( '#fullpage' ).fullpage( {
        navigation: true,
        slidesNavigation: true,
        anchors: [
            'home',
            'blog',
            'portfolio',
            'bio',
            'proficiencies',
            'contact',
        ],
        menu: '#myNavbar',
        controlArrows: true,
        responsiveWidth: 768,
        fixedElements: '#navWrapper',
        navigationTooltips: [
            'Home',
            'Blog',
            'Portfolio',
            'Bio',
            'Proficiencies',
            'Contact Me'
        ],
        afterRender: function ( ) {
            if ( $(window).width() <= 768 ) {
                var lastScrollTop = 0;

                $( window ).on( 'scroll', function ( event ) {
                    var st = $( this ).scrollTop();
                    if ( st < lastScrollTop ) {
                        $( '#myNavbar' ).slideDown();
                    }
                    else {
                        $( '#myNavbar' ).slideUp();
                    }
                    lastScrollTop = st;
                } );
            }
        }
    } );

    /**
     *
     * Sidebar toggle
     *
     */

    $( '.menuToggle' ).click( function () {
        $( '#mobileNav' ).toggleClass( 'w3-show' );
    } );
    
    /**
     * 
     * Manage featured blog post animations
     * 
     */
        
    $( '.featured' ).hover(function() {
        $( this ).toggleClass('show');
        var articleId = $( this ).data('article-id');
        $( this ).find('.title-link').toggleClass('w3-text-white');
        $( this ).find('.title-date').toggleClass('show');
    });
    
    /**
     * 
     * Manage animations on portfolio links
     * 
     */
     
    $( '.portfolio-animate' ).hover(function() {
       $( this ).toggleClass('shake'); 
    });
    
    

} );