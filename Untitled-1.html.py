<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CAFEPA Colombia • Café & Arepas Rellenas | Claymorphism UI</title>

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        clay: {
                            bg: '#F5EFE6',
                            card: '#FFFDF9',
                            coffee: '#7A4A32',
                            'coffee-light': '#9E6B4D',
                            cream: '#FFF5E4',
                            yellow: '#FFE699',
                            peach: '#FFC4A3',
                            mint: '#C1E1C1',
                            pink: '#FFB7B2',
                            purple: '#E2C2FF',
                            text: '#3D2C24',
                            muted: '#7C6A5D'
                        }
                    },
                    fontFamily: {
                        sans: ['Fredoka', 'Plus Jakarta Sans', 'sans-serif'],
                        display: ['Fredoka', 'sans-serif']
                    },
                    borderRadius: {
                        '4xl': '2.5rem',
                        '5xl': '3rem'
                    }
                }
            }
        }
    </script>

    <!-- Google Fonts & FontAwesome Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <style>
        body {
            background-color: #F5EFE6;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(255, 230, 153, 0.35) 0%, transparent 20%),
                radial-gradient(circle at 90% 80%, rgba(193, 225, 193, 0.35) 0%, transparent 25%),
                radial-gradient(circle at 50% 50%, rgba(255, 196, 163, 0.25) 0%, transparent 30%);
            background-attachment: fixed;
            color: #3D2C24;
            font-family: 'Fredoka', 'Plus Jakarta Sans', sans-serif;
            overflow-x: hidden;
        }

        /* 3D Soft Clay Card Style */
        .clay-card {
            background: #FFFDF9;
            border-radius: 2rem;
            box-shadow: 
                10px 10px 20px rgba(180, 160, 140, 0.25),
                -10px -10px 20px rgba(255, 255, 255, 0.95),
                inset 3px 3px 6px rgba(255, 255, 255, 0.9),
                inset -4px -4px 8px rgba(160, 140, 120, 0.08);
            border: 2px solid rgba(255, 255, 255, 0.8);
            transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .clay-card:hover {
            transform: translateY(-5px);
            box-shadow: 
                14px 14px 28px rgba(180, 160, 140, 0.3),
                -12px -12px 24px rgba(255, 255, 255, 0.95),
                inset 4px 4px 8px rgba(255, 255, 255, 0.9),
                inset -4px -4px 8px rgba(160, 140, 120, 0.08);
        }

        /* Clay Button Style */
        .clay-btn {
            border-radius: 9999px;
            box-shadow: 
                6px 6px 14px rgba(160, 140, 120, 0.28),
                -6px -6px 14px rgba(255, 255, 255, 0.9),
                inset 3px 3px 6px rgba(255, 255, 255, 0.7),
                inset -3px -3px 6px rgba(0, 0, 0, 0.1);
            border: 2px solid rgba(255, 255, 255, 0.6);
            transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
            cursor: pointer;
            user-select: none;
        }

        .clay-btn:hover {
            transform: scale(1.04) translateY(-2px);
            box-shadow: 
                8px 8px 18px rgba(160, 140, 120, 0.35),
                -8px -8px 18px rgba(255, 255, 255, 0.95),
                inset 3px 3px 6px rgba(255, 255, 255, 0.8),
                inset -3px -3px 6px rgba(0, 0, 0, 0.12);
        }

        .clay-btn:active, .clay-btn.active {
            transform: scale(0.96) translateY(2px);
            box-shadow: 
                2px 2px 6px rgba(160, 140, 120, 0.2),
                -2px -2px 6px rgba(255, 255, 255, 0.8),
                inset -3px -3px 6px rgba(255, 255, 255, 0.5),
                inset 4px 4px 8px rgba(0, 0, 0, 0.15);
        }

        /* Clay Inset Input/Container */
        .clay-inset {
            background: #F0E6D8;
            border-radius: 1.5rem;
            box-shadow: 
                inset 4px 4px 8px rgba(150, 130, 110, 0.25),
                inset -4px -4px 8px rgba(255, 255, 255, 0.9);
            border: 1.5px solid rgba(255, 255, 255, 0.5);
        }

        /* Soft Floating Clay Icon */
        .clay-badge {
            border-radius: 9999px;
            box-shadow: 
                4px 4px 8px rgba(160, 140, 120, 0.2),
                -4px -4px 8px rgba(255, 255, 255, 0.8),
                inset 2px 2px 4px rgba(255, 255, 255, 0.8),
                inset -2px -2px 4px rgba(0, 0, 0, 0.08);
        }

        /* Floating Bobbing Animation */
        @keyframes clayFloat {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-8px) rotate(1.5deg); }
        }

        .clay-float {
            animation: clayFloat 4s ease-in-out infinite;
        }

        .clay-float-delayed {
            animation: clayFloat 4.5s ease-in-out 1.5s infinite;
        }

        /* Custom Soft Scrollbar */
        ::-webkit-scrollbar {
            width: 14px;
        }
        ::-webkit-scrollbar-track {
            background: #F5EFE6;
        }
        ::-webkit-scrollbar-thumb {
            background: #D8C3B0;
            border-radius: 20px;
            border: 4px solid #F5EFE6;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #7A4A32;
        }
    </style>
</head>
<body class="selection:bg-clay-peach selection:text-clay-text">

    <!-- TOP CLAY ANNOUNCEMENT BANNER -->
    <div class="bg-clay-yellow py-2 px-4 border-b border-white/60 shadow-sm relative z-30 font-medium text-xs sm:text-sm text-clay-coffee">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <div class="flex items-center space-x-2 truncate">
                <span class="bg-clay-coffee text-white px-3 py-0.5 rounded-full text-xs font-bold clay-badge">🇨🇴 100% COLOMBIANO</span>
                <span class="hidden sm:inline font-bold">Café de Origen de Huila & Quindío • Arepas Rellenas en Budare</span>
                <span class="sm:hidden font-bold">Café de Origen & Arepas Rellenas</span>
            </div>
            <div class="flex items-center space-x-2 shrink-0">
                <span class="bg-white/80 text-clay-coffee px-3 py-0.5 rounded-full text-xs font-bold clay-badge">
                    ⚡ ENVÍOS BOGOTÁ, MEDELLÍN, CALI
                </span>
            </div>
        </div>
    </div>

    <!-- MAIN NAVIGATION HEADER (CENTERED LOGO) -->
    <header class="sticky top-0 z-40 bg-clay-bg/90 backdrop-blur-md py-3 px-4 sm:px-8 border-b border-white/40">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-4">
            
            <!-- Left Side: Nav Links -->
            <nav class="flex items-center space-x-2 font-bold text-xs uppercase tracking-wider order-2 md:order-1">
                <a href="#inicio" class="clay-btn bg-white text-clay-text px-4 py-2.5 flex items-center space-x-1.5">
                    <i class="fa-solid fa-house text-clay-coffee"></i>
                    <span>Inicio</span>
                </a>
                <a href="#menu" class="clay-btn bg-clay-cream text-clay-coffee px-4 py-2.5 flex items-center space-x-1.5">
                    <i class="fa-solid fa-utensils text-clay-coffee"></i>
                    <span>Menú</span>
                </a>
                <a href="#creador" class="clay-btn bg-clay-peach text-clay-coffee px-4 py-2.5 flex items-center space-x-1.5">
                    <i class="fa-solid fa-wand-magic-sparkles text-clay-coffee"></i>
                    <span>Armar Arepa</span>
                </a>
            </nav>

            <!-- CENTERED BRAND LOGO (CLAYMORPHISM PUFFY CAPSULE) -->
            <div class="order-1 md:order-2 w-full md:w-auto flex justify-center">
                <a href="#inicio" class="group focus:outline-none">
                    <div class="clay-btn bg-clay-cream px-6 py-2.5 flex items-center space-x-3 text-clay-coffee transform group-hover:scale-105 transition-all">
                        <!-- Soft Clay Mug Icon -->
                        <div class="w-10 h-10 bg-clay-coffee text-white rounded-full flex items-center justify-center text-lg clay-badge shadow-inner">
                            <i class="fa-solid fa-mug-hot"></i>
                        </div>
                        
                        <div class="text-center">
                            <span class="font-display font-extrabold text-2xl tracking-tight leading-none block text-clay-coffee">
                                CAFEPA
                            </span>
                            <span class="text-[9px] font-extrabold uppercase tracking-widest text-clay-coffee-light bg-clay-yellow/80 px-2 py-0.5 rounded-full block mt-0.5">
                                CAFÉ & AREPAS • COLOMBIA 🇨🇴
                            </span>
                        </div>

                        <!-- Soft Clay Arepa Icon -->
                        <div class="w-10 h-10 bg-clay-yellow text-clay-coffee rounded-full flex items-center justify-center text-lg clay-badge">
                            <i class="fa-solid fa-bread-slice"></i>
                        </div>
                    </div>
                </a>
            </div>

            <!-- Right Side: Social Media Icons & Cart Button -->
            <div class="flex items-center space-x-3 order-3">
                <!-- SOCIAL MEDIA CLAY ICONS -->
                <div class="flex items-center space-x-1.5">
                    <a href="https://instagram.com" target="_blank" rel="noopener" class="clay-btn bg-clay-pink text-clay-coffee w-10 h-10 flex items-center justify-center text-sm" title="Instagram CAFEPA">
                        <i class="fa-brands fa-instagram"></i>
                    </a>
                    <a href="https://facebook.com" target="_blank" rel="noopener" class="clay-btn bg-white text-clay-coffee w-10 h-10 flex items-center justify-center text-sm" title="Facebook CAFEPA">
                        <i class="fa-brands fa-facebook-f"></i>
                    </a>
                    <a href="https://tiktok.com" target="_blank" rel="noopener" class="clay-btn bg-clay-purple text-clay-coffee w-10 h-10 flex items-center justify-center text-sm" title="TikTok CAFEPA">
                        <i class="fa-brands fa-tiktok"></i>
                    </a>
                    <a href="https://wa.me/573001234567" target="_blank" rel="noopener" class="clay-btn bg-clay-mint text-clay-coffee w-10 h-10 flex items-center justify-center text-sm" title="WhatsApp Colombia">
                        <i class="fa-brands fa-whatsapp text-base"></i>
                    </a>
                </div>

                <!-- CART TRIGGER BUTTON -->
                <button id="cartBtn" class="clay-btn bg-clay-yellow px-4 py-2.5 text-xs font-black text-clay-coffee uppercase flex items-center space-x-2">
                    <i class="fa-solid fa-basket-shopping text-sm"></i>
                    <span class="hidden sm:inline">Pedido</span>
                    <span id="cartBadge" class="bg-clay-coffee text-white font-bold text-xs px-2 py-0.5 rounded-full clay-badge">0</span>
                </button>
            </div>

        </div>
    </header>

    <!-- HERO SECTION -->
    <section id="inicio" class="py-12 sm:py-16 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto relative">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            
            <!-- Left Text Content -->
            <div class="lg:col-span-7 space-y-6">
                
                <div class="inline-flex items-center space-x-2 bg-clay-cream px-4 py-2 rounded-full clay-badge text-clay-coffee font-bold text-xs uppercase tracking-wider">
                    <span class="w-3 h-3 bg-clay-mint rounded-full animate-ping"></span>
                    <span>🇨🇴 El Sabor Típico Colombiano en Su Máxima Expresión</span>
                </div>

                <h1 class="font-display font-extrabold text-4xl sm:text-6xl lg:text-7xl leading-tight text-clay-coffee">
                    CAFÉ DE ORIGEN <br>
                    <span class="inline-block bg-clay-yellow px-4 py-1 rounded-3xl clay-card text-clay-coffee my-1 transform -rotate-1">
                        RECIÉN COLADO
                    </span> <br>
                    & AREPAS RELLENAS
                </h1>

                <p class="text-base sm:text-lg font-medium text-clay-muted bg-white/70 p-6 rounded-3xl clay-card leading-relaxed">
                    ☕ Disfruta de la mejor combinación colombiana: granos de café 100% Arábigo cultivados en Huila y Quindío junto a crujientes arepas de maíz petaco tostadas al budare y rellenas de queso sabana, carne desmechada, chicharrón y hogao casero.
                </p>

                <!-- Action CTA Buttons -->
                <div class="flex flex-wrap gap-4 pt-2">
                    <a href="#menu" class="clay-btn bg-clay-yellow text-clay-coffee px-7 py-4 text-sm font-extrabold uppercase tracking-wider flex items-center space-x-2">
                        <i class="fa-solid fa-mug-hot text-base"></i>
                        <span>EXPLORAR MENÚ</span>
                    </a>
                    <a href="#creador" class="clay-btn bg-clay-mint text-clay-coffee px-7 py-4 text-sm font-extrabold uppercase tracking-wider flex items-center space-x-2">
                        <i class="fa-solid fa-wand-magic-sparkles text-base"></i>
                        <span>ARMAR MI AREPA</span>
                    </a>
                </div>

                <!-- Feature Pills -->
                <div class="grid grid-cols-3 gap-4 pt-2">
                    <div class="clay-card bg-clay-cream p-3 text-center">
                        <span class="font-extrabold text-clay-coffee text-base block">100%</span>
                        <span class="text-[11px] font-bold text-clay-muted uppercase block">Arábigo de Finca</span>
                    </div>
                    <div class="clay-card bg-clay-peach p-3 text-center">
                        <span class="font-extrabold text-clay-coffee text-base block">Budare</span>
                        <span class="text-[11px] font-bold text-clay-coffee block uppercase">Asado Caliente</span>
                    </div>
                    <div class="clay-card bg-clay-mint p-3 text-center">
                        <span class="font-extrabold text-clay-coffee text-base block">COP $</span>
                        <span class="text-[11px] font-bold text-clay-coffee block uppercase">Precios Justos</span>
                    </div>
                </div>

            </div>

            <!-- Right Visual 3D Clay Display Showcase -->
            <div class="lg:col-span-5 relative">
                <div class="clay-card bg-clay-cream p-6 relative space-y-4">
                    
                    <div class="flex justify-between items-center pb-2 border-b border-clay-coffee/10">
                        <span class="font-extrabold text-xs uppercase bg-clay-coffee text-white px-3 py-1 rounded-full clay-badge">
                            ESPECIALIDAD CAFEPA
                        </span>
                        <span class="font-extrabold text-xs bg-clay-yellow text-clay-coffee px-3 py-1 rounded-full clay-badge">
                            COLOMBIA 🇨🇴
                        </span>
                    </div>

                    <!-- Clay Styled Image Frame -->
                    <div class="relative clay-card overflow-hidden h-72 bg-white">
                        <img src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=800&q=80" 
                             alt="Café Colombiano y Arepa" class="w-full h-full object-cover">
                        <div class="absolute bottom-3 left-3 bg-clay-bg/90 backdrop-blur-md px-3 py-1.5 rounded-2xl clay-badge text-clay-coffee font-extrabold text-xs">
                            ☕ Tinto Fresco + 🫓 Arepa Paisa
                        </div>
                    </div>

                    <!-- Quote Pill -->
                    <div class="clay-card bg-white p-4 text-center">
                        <p class="font-extrabold text-xs text-clay-coffee uppercase tracking-wide">
                            "El aroma del café recien colado y la arepa crujiente con queso derretido."
                        </p>
                    </div>

                    <!-- Floating 3D Badge -->
                    <div class="absolute -top-4 -right-4 clay-btn bg-clay-pink text-clay-coffee font-extrabold text-center text-xs p-4 w-20 h-20 rounded-full flex flex-col justify-center items-center clay-float">
                        <span>100%</span>
                        <span class="text-[10px]">TÍPICO</span>
                    </div>

                </div>
            </div>

        </div>
    </section>

    <!-- MENU SECTION -->
    <section id="menu" class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Header Title -->
        <div class="text-center max-w-3xl mx-auto mb-10 space-y-3">
            <span class="bg-clay-yellow text-clay-coffee font-bold text-xs px-4 py-1.5 rounded-full clay-badge uppercase tracking-widest inline-block">
                MENÚ OFICIAL COLOMBIA
            </span>
            <h2 class="font-display font-extrabold text-3xl sm:text-5xl text-clay-coffee">
                NUESTRO MENÚ DELICIOSO
            </h2>
            <p class="text-clay-muted font-medium text-sm sm:text-base">
                Elige entre nuestras bebidas de café de especialidad de origen y nuestras famosas arepas colombianas hechas en budare.
            </p>
        </div>

        <!-- CATEGORY SWITCHER & SEARCH BAR -->
        <div class="clay-card bg-clay-cream p-5 mb-10">
            <div class="flex flex-col lg:flex-row items-center justify-between gap-4">
                
                <!-- Category Tabs (Todos / Bebidas - Café / Comidas - Arepas) -->
                <div class="flex flex-wrap justify-center gap-3 w-full lg:w-auto" id="categoryTabs">
                    <button data-category="todos" class="category-btn active clay-btn bg-clay-yellow px-5 py-3 font-extrabold text-xs uppercase tracking-wider text-clay-coffee flex items-center space-x-2">
                        <i class="fa-solid fa-border-all"></i>
                        <span>Todos los Productos</span>
                    </button>
                    
                    <button data-category="bebida" class="category-btn clay-btn bg-white px-5 py-3 font-extrabold text-xs uppercase tracking-wider text-clay-coffee flex items-center space-x-2">
                        <i class="fa-solid fa-mug-hot text-clay-coffee-light text-sm"></i>
                        <span>☕ Bebidas (Café de Origen)</span>
                    </button>
                    
                    <button data-category="comida" class="category-btn clay-btn bg-white px-5 py-3 font-extrabold text-xs uppercase tracking-wider text-clay-coffee flex items-center space-x-2">
                        <i class="fa-solid fa-bread-slice text-clay-peach text-sm"></i>
                        <span>🫓 Comida (Arepas Rellenas)</span>
                    </button>
                </div>

                <!-- Clay Search Input -->
                <div class="w-full lg:w-80 relative">
                    <div class="clay-inset p-2.5 flex items-center bg-white/80">
                        <i class="fa-solid fa-magnifying-glass text-clay-coffee px-2 text-sm"></i>
                        <input type="text" id="searchInput" placeholder="Buscar tinto, carne, choclo..." 
                               class="w-full bg-transparent text-clay-coffee font-bold text-xs focus:outline-none placeholder-clay-muted uppercase">
                    </div>
                </div>

            </div>
        </div>

        <!-- MENU CARDS GRID -->
        <div id="menuGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <!-- Injected by JavaScript -->
        </div>

        <!-- Empty Search State -->
        <div id="emptyState" class="hidden text-center py-12 clay-card bg-white p-8 max-w-md mx-auto">
            <div class="w-16 h-16 bg-clay-pink text-clay-coffee rounded-full flex items-center justify-center mx-auto mb-4 text-2xl clay-badge">
                <i class="fa-solid fa-face-frown"></i>
            </div>
            <h3 class="text-xl font-extrabold text-clay-coffee">SIN RESULTADOS</h3>
            <p class="text-clay-muted font-medium text-xs mt-2">No encontramos productos con ese nombre. Intenta buscar 'tinto', 'choclo' o 'paisa'.</p>
        </div>

    </section>

    <!-- AREPA CUSTOMIZER SECTION -->
    <section id="creador" class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="clay-card bg-clay-cream p-6 sm:p-10">
            
            <div class="text-center max-w-3xl mx-auto mb-10 space-y-3">
                <span class="bg-clay-mint text-clay-coffee font-bold text-xs px-4 py-1.5 rounded-full clay-badge uppercase tracking-widest inline-block">
                    ⚡ CREADOR INTERACTIVO
                </span>
                <h2 class="font-display font-extrabold text-3xl sm:text-5xl text-clay-coffee">
                    ARMA TU AREPA COLOMBIANA
                </h2>
                <p class="text-clay-muted font-medium text-sm">Elige el tipo de masa base y combínala con tus ingredientes y rellenos preferidos.</p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                
                <!-- Controls Column -->
                <div class="lg:col-span-7 space-y-6">
                    
                    <!-- 1. MASA BASE -->
                    <div class="clay-card bg-white p-6 space-y-4">
                        <span class="font-extrabold text-xs uppercase bg-clay-yellow text-clay-coffee px-3 py-1 rounded-full clay-badge inline-block">
                            1. SELECCIONA MASA BASE:
                        </span>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3" id="builderBase">
                            <button data-type="arepa" data-price="12000" class="builder-base-btn active clay-btn bg-clay-yellow p-4 text-left font-extrabold text-clay-coffee">
                                <div class="text-sm uppercase">Masa Maíz Petaco Blanco</div>
                                <div class="text-xs font-bold text-clay-coffee-light mt-1">$12.000 COP</div>
                            </button>
                            <button data-type="choclo" data-price="11000" class="builder-base-btn clay-btn bg-white p-4 text-left font-extrabold text-clay-coffee">
                                <div class="text-sm uppercase">Masa Choclo Dulce Tierno</div>
                                <div class="text-xs font-bold text-clay-coffee-light mt-1">$11.000 COP</div>
                            </button>
                        </div>
                    </div>

                    <!-- 2. RELLENOS Y TOPPINGS -->
                    <div class="clay-card bg-white p-6 space-y-4">
                        <span class="font-extrabold text-xs uppercase bg-clay-mint text-clay-coffee px-3 py-1 rounded-full clay-badge inline-block">
                            2. ELIGE TUS RELLENOS Y TOPPINGS:
                        </span>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3" id="builderFillings">
                            <label class="clay-btn bg-white p-3 flex items-center space-x-3 cursor-pointer">
                                <input type="checkbox" data-name="Carne Desmechada" data-price="4000" class="builder-topping w-5 h-5 accent-clay-coffee">
                                <span class="text-xs font-bold uppercase text-clay-coffee">Carne Desmechada (+$4k)</span>
                            </label>
                            <label class="clay-btn bg-white p-3 flex items-center space-x-3 cursor-pointer">
                                <input type="checkbox" data-name="Queso Sabana" data-price="3000" class="builder-topping w-5 h-5 accent-clay-coffee" checked>
                                <span class="text-xs font-bold uppercase text-clay-coffee">Queso Sabana (+$3k)</span>
                            </label>
                            <label class="clay-btn bg-white p-3 flex items-center space-x-3 cursor-pointer">
                                <input type="checkbox" data-name="Chicharrón Crocante" data-price="4500" class="builder-topping w-5 h-5 accent-clay-coffee">
                                <span class="text-xs font-bold uppercase text-clay-coffee">Chicharrón (+$4.5k)</span>
                            </label>
                            <label class="clay-btn bg-white p-3 flex items-center space-x-3 cursor-pointer">
                                <input type="checkbox" data-name="Pollo Criollo" data-price="3500" class="builder-topping w-5 h-5 accent-clay-coffee">
                                <span class="text-xs font-bold uppercase text-clay-coffee">Pollo Criollo (+$3.5k)</span>
                            </label>
                            <label class="clay-btn bg-white p-3 flex items-center space-x-3 cursor-pointer">
                                <input type="checkbox" data-name="Guacamole Casero" data-price="2500" class="builder-topping w-5 h-5 accent-clay-coffee">
                                <span class="text-xs font-bold uppercase text-clay-coffee">Guacamole (+$2.5k)</span>
                            </label>
                            <label class="clay-btn bg-white p-3 flex items-center space-x-3 cursor-pointer">
                                <input type="checkbox" data-name="Suero Costeño" data-price="2000" class="builder-topping w-5 h-5 accent-clay-coffee">
                                <span class="text-xs font-bold uppercase text-clay-coffee">Suero Costeño (+$2k)</span>
                            </label>
                        </div>
                    </div>

                </div>

                <!-- Preview Box Column -->
                <div class="lg:col-span-5 sticky top-24">
                    <div class="clay-card bg-clay-peach p-6 text-center space-y-4">
                        <div class="w-20 h-20 bg-clay-coffee text-white rounded-full mx-auto flex items-center justify-center text-3xl clay-badge">
                            <i class="fa-solid fa-bread-slice"></i>
                        </div>
                        
                        <div>
                            <span class="bg-white text-clay-coffee font-bold text-[10px] px-3 py-1 rounded-full clay-badge uppercase">
                                PREVISUALIZACIÓN DE TU AREPA
                            </span>
                            <h3 id="customTitle" class="font-display font-extrabold text-2xl uppercase text-clay-coffee mt-2">Masa Maíz Petaco Blanco</h3>
                            <p id="customDescription" class="text-xs font-bold text-clay-coffee-light mt-1">Con: Queso Sabana</p>
                        </div>

                        <div class="clay-card bg-white p-4 flex justify-between items-center font-bold text-sm text-clay-coffee">
                            <span>TOTAL ESTIMADO:</span>
                            <span id="customPrice" class="text-base bg-clay-yellow px-3 py-1 rounded-full clay-badge text-clay-coffee font-extrabold">$15.000 COP</span>
                        </div>

                        <button id="addCustomToCartBtn" class="w-full clay-btn bg-clay-coffee text-white font-extrabold py-4 text-xs uppercase tracking-wider flex items-center justify-center space-x-2">
                            <i class="fa-solid fa-plus text-base"></i>
                            <span>AGREGAR AREPA CREADA AL PEDIDO</span>
                        </button>
                    </div>
                </div>

            </div>

        </div>
    </section>

    <!-- COLOMBIAN ORIGIN STORY -->
    <section class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="clay-card bg-white p-8 sm:p-12">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
                
                <div class="space-y-5">
                    <span class="bg-clay-yellow text-clay-coffee font-bold text-xs px-3.5 py-1.5 rounded-full clay-badge uppercase tracking-widest inline-block">
                        🇨🇴 TRADICIÓN DE MONTAÑA
                    </span>

                    <h2 class="font-display font-extrabold text-3xl sm:text-5xl text-clay-coffee leading-tight">
                        DEL CAFETAL Y EL BUDARE A TU MESA
                    </h2>

                    <p class="font-medium text-clay-muted text-sm sm:text-base leading-relaxed">
                        Seleccionamos exclusivamente lotes de café Arábigo cultivados por encima de los 1.700m en Huila y Quindío. Tostamos en lotes pequeños para garantizar dulzor natural de panela y notas aromáticas cítricas.
                    </p>

                    <p class="font-medium text-clay-muted text-sm sm:text-base leading-relaxed">
                        Nuestras arepas se muelen y amasan cada mañana con maíz 100% natural sin conservantes. Doradas en budares de hierro caliente a fuego alto.
                    </p>

                    <div class="grid grid-cols-2 gap-4 pt-2">
                        <div class="clay-card bg-clay-cream p-4">
                            <i class="fa-solid fa-seedling text-2xl text-clay-coffee mb-2"></i>
                            <h4 class="font-extrabold text-clay-coffee text-xs uppercase">100% ARÁBIGO LAVADO</h4>
                            <p class="text-[11px] font-bold text-clay-muted">Cosecha Selecta</p>
                        </div>
                        <div class="clay-card bg-clay-peach p-4">
                            <i class="fa-solid fa-fire text-2xl text-clay-coffee mb-2"></i>
                            <h4 class="font-extrabold text-clay-coffee text-xs uppercase">BUDARE TRADICIONAL</h4>
                            <p class="text-[11px] font-bold text-clay-coffee">Maíz Natural</p>
                        </div>
                    </div>
                </div>

                <!-- Clay Image Frame -->
                <div class="clay-card bg-clay-cream p-4">
                    <div class="relative clay-card overflow-hidden h-80 bg-white">
                        <img src="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=800&q=80" 
                             alt="Tinto Colombiano Tradicional" class="w-full h-full object-cover">
                        <div class="absolute bottom-4 left-4 right-4 bg-white/90 backdrop-blur-md p-3 rounded-2xl clay-badge text-clay-coffee">
                            <p class="font-bold text-xs uppercase text-clay-coffee-light">Orgullo Nacional</p>
                            <p class="font-extrabold text-sm uppercase">Tinto de Finca & Arepa Recién Hecha 🇨🇴</p>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- LOCATIONS IN COLOMBIA -->
    <section id="sedes" class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 space-y-2">
            <span class="bg-clay-pink text-clay-coffee font-bold text-xs px-3.5 py-1.5 rounded-full clay-badge uppercase tracking-widest inline-block">
                📍 PUNTOS DE VENTA EN COLOMBIA
            </span>
            <h2 class="font-display font-extrabold text-3xl sm:text-4xl text-clay-coffee">NUESTRAS SEDES</h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            
            <!-- Bogotá -->
            <div class="clay-card bg-white p-6 space-y-3">
                <div class="w-12 h-12 bg-clay-yellow text-clay-coffee rounded-full flex items-center justify-center font-extrabold text-xl clay-badge">
                    <i class="fa-solid fa-building-columns"></i>
                </div>
                <h3 class="font-extrabold text-lg text-clay-coffee uppercase">BOGOTÁ • ZONA ROSA</h3>
                <p class="text-xs font-bold text-clay-muted">Calle 10 #4-35 • Chapinero. Espacio con terraza, enchufes y ambiente pet friendly.</p>
                <div class="bg-clay-cream text-clay-coffee font-bold text-[11px] p-2 rounded-full text-center clay-badge uppercase">
                    HORARIO: 7:00 AM - 9:30 PM
                </div>
            </div>

            <!-- Medellín -->
            <div class="clay-card bg-white p-6 space-y-3">
                <div class="w-12 h-12 bg-clay-mint text-clay-coffee rounded-full flex items-center justify-center font-extrabold text-xl clay-badge">
                    <i class="fa-solid fa-mountain-sun"></i>
                </div>
                <h3 class="font-extrabold text-lg text-clay-coffee uppercase">MEDELLÍN • EL POBLADO</h3>
                <p class="text-xs font-bold text-clay-muted">Carrera 37 #8-12 • Vía Primavera. Barra especial de filtrados V60 y Chemex.</p>
                <div class="bg-clay-cream text-clay-coffee font-bold text-[11px] p-2 rounded-full text-center clay-badge uppercase">
                    HORARIO: 7:30 AM - 10:00 PM
                </div>
            </div>

            <!-- Cali -->
            <div class="clay-card bg-white p-6 space-y-3">
                <div class="w-12 h-12 bg-clay-peach text-clay-coffee rounded-full flex items-center justify-center font-extrabold text-xl clay-badge">
                    <i class="fa-solid fa-sun"></i>
                </div>
                <h3 class="font-extrabold text-lg text-clay-coffee uppercase">CALI • GRANADA</h3>
                <p class="text-xs font-bold text-clay-muted">Avenida 9N #15-22. Granizados de café helado y budare de arepas al aire libre.</p>
                <div class="bg-clay-cream text-clay-coffee font-bold text-[11px] p-2 rounded-full text-center clay-badge uppercase">
                    HORARIO: 8:00 AM - 9:00 PM
                </div>
            </div>

        </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-clay-coffee text-white py-12 px-4 sm:px-6 lg:px-8 text-xs font-medium">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
            
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 bg-clay-yellow text-clay-coffee rounded-full flex items-center justify-center font-extrabold text-lg clay-badge">
                    <i class="fa-solid fa-mug-hot"></i>
                </div>
                <span class="font-display font-extrabold text-2xl text-clay-cream tracking-tight">CAFEPA</span>
                <span class="bg-clay-pink text-clay-coffee px-2.5 py-0.5 rounded-full text-[10px] font-bold clay-badge">COLOMBIA 🇨🇴</span>
            </div>

            <p class="font-bold text-clay-cream/80 text-center">
                © <span id="currentYear"></span> CAFEPA COLOMBIA. TODOS LOS DERECHOS RESERVADOS.
            </p>

            <!-- FOOTER SOCIAL MEDIA CLAY BUTTONS -->
            <div class="flex space-x-2">
                <a href="https://instagram.com" target="_blank" class="clay-btn bg-clay-pink text-clay-coffee w-9 h-9 flex items-center justify-center">
                    <i class="fa-brands fa-instagram"></i>
                </a>
                <a href="https://facebook.com" target="_blank" class="clay-btn bg-white text-clay-coffee w-9 h-9 flex items-center justify-center">
                    <i class="fa-brands fa-facebook-f"></i>
                </a>
                <a href="https://tiktok.com" target="_blank" class="clay-btn bg-clay-yellow text-clay-coffee w-9 h-9 flex items-center justify-center">
                    <i class="fa-brands fa-tiktok"></i>
                </a>
                <a href="https://wa.me/573001234567" target="_blank" class="clay-btn bg-clay-mint text-clay-coffee w-9 h-9 flex items-center justify-center">
                    <i class="fa-brands fa-whatsapp"></i>
                </a>
            </div>

        </div>
    </footer>

    <!-- CART DRAWER (CLAYMORPHISM STYLE) -->
    <div id="cartDrawerOverlay" class="fixed inset-0 bg-clay-coffee/40 backdrop-blur-sm z-50 opacity-0 pointer-events-none transition-opacity duration-300"></div>

    <div id="cartDrawer" class="fixed top-0 right-0 h-full w-full max-w-md bg-clay-bg z-50 shadow-2xl transform translate-x-full transition-transform duration-300 flex flex-col p-4 sm:p-6">
        
        <!-- Header -->
        <div class="pb-4 border-b border-clay-coffee/10 flex justify-between items-center">
            <div class="flex items-center space-x-2">
                <div class="w-8 h-8 bg-clay-yellow text-clay-coffee rounded-full flex items-center justify-center text-sm clay-badge">
                    <i class="fa-solid fa-basket-shopping"></i>
                </div>
                <h3 class="font-display font-extrabold text-clay-coffee text-lg uppercase">TU PEDIDO CAFEPA</h3>
            </div>
            <button id="closeCartBtn" class="clay-btn bg-white text-clay-coffee w-9 h-9 flex items-center justify-center font-extrabold">
                <i class="fa-solid fa-xmark"></i>
            </button>
        </div>

        <!-- Receipt / Cart Body -->
        <div class="flex-1 overflow-y-auto py-4 space-y-4 text-xs font-medium">
            <div class="clay-card bg-white p-5 space-y-4">
                <div class="text-center border-b border-dashed border-clay-coffee/20 pb-3">
                    <p class="font-extrabold text-base text-clay-coffee uppercase">*** CAFEPA COLOMBIA ***</p>
                    <p class="font-bold text-clay-muted">Calle 10 #4-35 • Zona Rosa</p>
                    <p class="font-bold text-clay-coffee-light mt-1" id="receiptDate"></p>
                </div>

                <!-- Items Container -->
                <div id="cartItemsList" class="space-y-3">
                    <!-- Injected by JavaScript -->
                </div>

                <!-- Empty State Message -->
                <div id="emptyCartMessage" class="text-center py-8">
                    <i class="fa-solid fa-basket-shopping text-clay-muted text-4xl mb-2"></i>
                    <p class="font-extrabold text-clay-coffee text-sm uppercase">TU CARRITO ESTÁ VACÍO</p>
                    <p class="text-[11px] font-bold text-clay-muted mt-1">Explora nuestro menú y agrega tus café y arepas favoritas.</p>
                </div>

                <!-- Totals -->
                <div class="border-t border-dashed border-clay-coffee/20 pt-3 space-y-1.5 font-bold">
                    <div class="flex justify-between text-clay-muted">
                        <span>SUBTOTAL:</span>
                        <span id="cartSubtotal">$0 COP</span>
                    </div>
                    <div class="flex justify-between font-extrabold text-base text-clay-coffee pt-2 border-t border-clay-coffee/20">
                        <span>TOTAL A PAGAR:</span>
                        <span id="cartTotal" class="bg-clay-yellow px-3 py-1 rounded-full clay-badge text-clay-coffee">$0 COP</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Checkout Button -->
        <div class="pt-4 border-t border-clay-coffee/10">
            <button id="checkoutBtn" class="w-full clay-btn bg-clay-mint text-clay-coffee font-extrabold py-4 text-xs tracking-wider uppercase flex items-center justify-center space-x-2">
                <i class="fa-brands fa-whatsapp text-lg"></i>
                <span>ENVIAR PEDIDO POR WHATSAPP</span>
            </button>
        </div>

    </div>

    <!-- TOAST NOTIFICATION -->
    <div id="toast" class="fixed bottom-6 right-6 clay-card bg-clay-yellow p-4 z-50 transform translate-y-20 opacity-0 transition-all duration-300 flex items-center space-x-3">
        <span class="w-3 h-3 bg-clay-coffee rounded-full animate-ping"></span>
        <span id="toastMsg" class="text-xs font-extrabold text-clay-coffee uppercase">Producto añadido</span>
    </div>

    <!-- JAVASCRIPT APP LOGIC -->
    <script>
        // MENU DATA: CATEGORIZED BY BEBIDA (CAFÉ) AND COMIDA (AREPAS RELLENAS COLOMBIANAS)
        const menuItems = [
            // ================= BEBIDAS (CAFÉ DE ORIGEN COLOMBIANO) =================
            {
                id: 1,
                name: "Tinto Campesino Panela & Canela",
                category: "bebida",
                price: 4500,
                description: "Café suave del Huila preparado con melao de panela orgánica y astilla de canela.",
                image: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=600&q=80",
                badge: "TRADICIONAL"
            },
            {
                id: 2,
                name: "Café Perico Tradicional",
                category: "bebida",
                price: 5500,
                description: "Clásico perico colombiano: espresso cremoso combinado con leche tibia y microespuma.",
                image: "https://images.unsplash.com/photo-1534778101976-62847782c213?auto=format&fit=crop&w=600&q=80",
                badge: "MÁS VENDIDO"
            },
            {
                id: 3,
                name: "Espresso Doble Origen Quindío",
                category: "bebida",
                price: 6000,
                description: "Extracción intensa de granos lavados con crema dorada y notas aromáticas a chocolate.",
                image: "https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?auto=format&fit=crop&w=600&q=80"
            },
            {
                id: 4,
                name: "Cappuccino del Eje Cafetero",
                category: "bebida",
                price: 7500,
                description: "Shot de espresso doble con leche vaporizada y espolvoreado de cacao artesanal.",
                image: "https://images.unsplash.com/photo-1572490122747-3968b75cc699?auto=format&fit=crop&w=600&q=80"
            },
            {
                id: 5,
                name: "Caramel Latte Macchiato",
                category: "bebida",
                price: 8500,
                description: "Capas de leche cremosa, espresso cargado y hilos de arequipe colombiano casero.",
                image: "https://images.unsplash.com/photo-1570968915860-54d5c301fa9f?auto=format&fit=crop&w=600&q=80"
            },
            {
                id: 6,
                name: "Frappé CAFEPA Arequipe & Cacao",
                category: "bebida",
                price: 9500,
                description: "Bebida helada frapeada con espresso, arequipe criollo y crema chantilly.",
                image: "https://images.unsplash.com/photo-1517701604599-bb29b565090c?auto=format&fit=crop&w=600&q=80",
                badge: "FRÍO 🔥"
            },

            // ================= COMIDA (AREPAS RELLENAS COLOMBIANAS) =================
            {
                id: 7,
                name: "Arepa Paisa Carne Desmechada",
                category: "comida",
                price: 14000,
                description: "Arepa de maíz blanco petaco rellena de jugosa carne desmechada en hogao y queso costeño.",
                image: "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=600&q=80",
                badge: "TOP 1 🏆"
            },
            {
                id: 8,
                name: "Arepa de Choclo con Queso Sabana",
                category: "comida",
                price: 11000,
                description: "Arepa dulce de maíz tierno asada a la plancha con abundante queso sabana derretido.",
                image: "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=600&q=80",
                badge: "DULCE & SALADO"
            },
            {
                id: 9,
                name: "Arepa Rellena Pollo & Champiñón",
                category: "comida",
                price: 13500,
                description: "Pechuga de pollo desmechada en salsa de champiñones gratinada con queso mozzarella.",
                image: "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=600&q=80"
            },
            {
                id: 10,
                name: "Arepa de Huevo Costeña Especial",
                category: "comida",
                price: 9000,
                description: "Frita crujiente con huevo entero fresco y carne molida sazonada, servida con suero.",
                image: "https://images.unsplash.com/photo-1509722747041-616f39b57569?auto=format&fit=crop&w=600&q=80",
                badge: "CARIBE 🇨🇴"
            },
            {
                id: 11,
                name: "Arepa Trifásica (Carne+Pollo+Chicharrón)",
                category: "comida",
                price: 16500,
                description: "La reina CAFEPA: carne desmechada, pollo criollo, chicharrón crocante y guacamole.",
                image: "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=600&q=80",
                badge: "ESPECIALIDAD"
            },
            {
                id: 12,
                name: "Arepa Santandereana Chicharrón",
                category: "comida",
                price: 14500,
                description: "Masa con chicharrón molido y yuca, asada en budare y rellena con queso campesino.",
                image: "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?auto=format&fit=crop&w=600&q=80"
            }
        ];

        let cart = [];
        let currentCategory = 'todos';
        let searchQuery = '';

        // Web Audio Soft Synthesizer for Clay Sound Interaction
        function playClayPop() {
            try {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                if (!AudioContext) return;
                const ctx = new AudioContext();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();

                osc.type = 'sine';
                osc.frequency.setValueAtTime(320, ctx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(180, ctx.currentTime + 0.08);

                gain.gain.setValueAtTime(0.12, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.08);

                osc.connect(gain);
                gain.connect(ctx.destination);

                osc.start();
                osc.stop(ctx.currentTime + 0.08);
            } catch(e) {}
        }

        document.addEventListener('DOMContentLoaded', () => {
            document.getElementById('currentYear').textContent = new Date().getFullYear();
            document.getElementById('receiptDate').textContent = new Date().toLocaleDateString('es-CO', {
                day: 'numeric', month: 'short', year: 'numeric'
            });

            renderMenu();
            updateCartUI();
            setupCustomizer();

            // Sound feedback on all clay buttons
            document.querySelectorAll('button, .clay-btn, a').forEach(btn => {
                btn.addEventListener('click', () => playClayPop());
            });

            // Category Tab Switchers
            const tabs = document.querySelectorAll('.category-btn');
            tabs.forEach(tab => {
                tab.addEventListener('click', (e) => {
                    tabs.forEach(t => {
                        t.classList.remove('active', 'bg-clay-yellow');
                        t.classList.add('bg-white');
                    });
                    const btn = e.currentTarget;
                    btn.classList.add('active', 'bg-clay-yellow');
                    btn.classList.remove('bg-white');

                    currentCategory = btn.getAttribute('data-category');
                    renderMenu();
                });
            });

            // Menu Search Listener
            const searchInput = document.getElementById('searchInput');
            searchInput.addEventListener('input', (e) => {
                searchQuery = e.target.value.toLowerCase().trim();
                renderMenu();
            });

            // Cart Drawer Controls
            const cartBtn = document.getElementById('cartBtn');
            const closeCartBtn = document.getElementById('closeCartBtn');
            const overlay = document.getElementById('cartDrawerOverlay');
            const drawer = document.getElementById('cartDrawer');

            const openCart = () => {
                drawer.classList.remove('translate-x-full');
                overlay.classList.remove('opacity-0', 'pointer-events-none');
            };

            const closeCart = () => {
                drawer.classList.add('translate-x-full');
                overlay.classList.add('opacity-0', 'pointer-events-none');
            };

            cartBtn.addEventListener('click', openCart);
            closeCartBtn.addEventListener('click', closeCart);
            overlay.addEventListener('click', closeCart);

            document.getElementById('checkoutBtn').addEventListener('click', sendWhatsAppOrder);
        });

        function formatCOP(amount) {
            return '$' + amount.toLocaleString('es-CO') + ' COP';
        }

        function renderMenu() {
            const menuGrid = document.getElementById('menuGrid');
            const emptyState = document.getElementById('emptyState');

            const filteredItems = menuItems.filter(item => {
                const matchesCategory = (currentCategory === 'todos' || item.category === currentCategory);
                const matchesSearch = item.name.toLowerCase().includes(searchQuery) || item.description.toLowerCase().includes(searchQuery);
                return matchesCategory && matchesSearch;
            });

            if (filteredItems.length === 0) {
                menuGrid.innerHTML = '';
                emptyState.classList.remove('hidden');
                return;
            }

            emptyState.classList.add('hidden');

            menuGrid.innerHTML = filteredItems.map(item => `
                <div class="clay-card bg-white p-5 flex flex-col justify-between">
                    <div>
                        <div class="relative h-44 clay-card overflow-hidden bg-clay-cream mb-4">
                            <img src="${item.image}" alt="${item.name}" class="w-full h-full object-cover">
                            ${item.badge ? `
                                <span class="absolute top-3 left-3 bg-clay-yellow text-clay-coffee font-bold text-[10px] uppercase px-3 py-1 rounded-full clay-badge">
                                    ${item.badge}
                                </span>
                            ` : ''}
                            <div class="absolute bottom-3 right-3 bg-white/90 backdrop-blur-md text-clay-coffee font-extrabold text-xs px-3 py-1 rounded-full clay-badge">
                                ${formatCOP(item.price)}
                            </div>
                        </div>

                        <div class="space-y-1.5 mb-4">
                            <div class="font-extrabold text-[10px] uppercase text-clay-coffee-light tracking-wider">
                                <i class="${item.category === 'bebida' ? 'fa-solid fa-mug-hot' : 'fa-solid fa-bread-slice'} mr-1"></i>
                                ${item.category === 'bebida' ? 'Café de Origen' : 'Arepa Rellena'}
                            </div>
                            <h3 class="font-display font-extrabold text-clay-coffee text-base leading-snug">${item.name}</h3>
                            <p class="text-clay-muted text-xs font-medium leading-relaxed">${item.description}</p>
                        </div>
                    </div>

                    <button onclick="addToCart(${item.id})" class="w-full clay-btn bg-clay-yellow py-3 px-4 font-extrabold text-xs uppercase tracking-wider flex items-center justify-center space-x-2 text-clay-coffee">
                        <i class="fa-solid fa-plus text-sm"></i>
                        <span>AGREGAR AL PEDIDO</span>
                    </button>
                </div>
            `).join('');
        }

        function addToCart(itemId) {
            const item = menuItems.find(i => i.id === itemId);
            if (!item) return;

            const existingIndex = cart.findIndex(c => c.id === itemId);
            if (existingIndex > -1) {
                cart[existingIndex].quantity += 1;
            } else {
                cart.push({ ...item, quantity: 1 });
            }

            updateCartUI();
            showToast(`AÑADIDO: ${item.name}`);
        }

        function changeQuantity(index, delta) {
            if (cart[index]) {
                cart[index].quantity += delta;
                if (cart[index].quantity <= 0) {
                    cart.splice(index, 1);
                }
            }
            updateCartUI();
        }

        function updateCartUI() {
            const cartItemsList = document.getElementById('cartItemsList');
            const emptyCartMessage = document.getElementById('emptyCartMessage');
            const cartBadge = document.getElementById('cartBadge');
            const cartSubtotal = document.getElementById('cartSubtotal');
            const cartTotal = document.getElementById('cartTotal');

            const totalCount = cart.reduce((acc, curr) => acc + curr.quantity, 0);
            const totalPrice = cart.reduce((acc, curr) => acc + (curr.price * curr.quantity), 0);

            cartBadge.textContent = totalCount;

            if (cart.length === 0) {
                cartItemsList.innerHTML = '';
                emptyCartMessage.classList.remove('hidden');
            } else {
                emptyCartMessage.classList.add('hidden');
                cartItemsList.innerHTML = cart.map((item, idx) => `
                    <div class="flex items-center justify-between py-2 border-b border-clay-coffee/10">
                        <div class="pr-2">
                            <p class="font-extrabold text-clay-coffee text-xs uppercase">${item.name}</p>
                            <p class="text-[10px] font-bold text-clay-muted">${item.quantity} x ${formatCOP(item.price)}</p>
                        </div>

                        <div class="flex items-center space-x-1 shrink-0">
                            <button onclick="changeQuantity(${idx}, -1)" class="w-6 h-6 clay-btn bg-white font-extrabold text-xs text-clay-coffee flex items-center justify-center">
                                -
                            </button>
                            <span class="font-extrabold text-xs w-5 text-center text-clay-coffee">${item.quantity}</span>
                            <button onclick="changeQuantity(${idx}, 1)" class="w-6 h-6 clay-btn bg-white font-extrabold text-xs text-clay-coffee flex items-center justify-center">
                                +
                            </button>
                        </div>
                    </div>
                `).join('');
            }

            cartSubtotal.textContent = formatCOP(totalPrice);
            cartTotal.textContent = formatCOP(totalPrice);
        }

        function setupCustomizer() {
            const baseButtons = document.querySelectorAll('.builder-base-btn');
            const toppings = document.querySelectorAll('.builder-topping');
            const titleEl = document.getElementById('customTitle');
            const descEl = document.getElementById('customDescription');
            const priceEl = document.getElementById('customPrice');
            const addBtn = document.getElementById('addCustomToCartBtn');

            let currentBase = { name: "Masa Maíz Petaco Blanco", price: 12000 };

            function updateCustomPreview() {
                let basePrice = currentBase.price;
                let selectedToppings = [];
                let toppingTotal = 0;

                toppings.forEach(top => {
                    if (top.checked) {
                        const tName = top.getAttribute('data-name');
                        const tPrice = parseInt(top.getAttribute('data-price'));
                        selectedToppings.push(tName);
                        toppingTotal += tPrice;
                    }
                });

                const finalPrice = basePrice + toppingTotal;

                titleEl.textContent = currentBase.name;
                descEl.textContent = selectedToppings.length > 0 
                    ? "Con: " + selectedToppings.join(', ')
                    : "Sin adicionales";
                priceEl.textContent = formatCOP(finalPrice);
            }

            baseButtons.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    baseButtons.forEach(b => {
                        b.classList.remove('active', 'bg-clay-yellow');
                        b.classList.add('bg-white');
                    });
                    const target = e.currentTarget;
                    target.classList.add('active', 'bg-clay-yellow');
                    target.classList.remove('bg-white');

                    const type = target.getAttribute('data-type');
                    const price = parseInt(target.getAttribute('data-price'));
                    currentBase = {
                        name: type === 'arepa' ? 'Masa Maíz Petaco Blanco' : 'Masa Choclo Dulce Tierno',
                        price: price
                    };
                    updateCustomPreview();
                });
            });

            toppings.forEach(top => {
                top.addEventListener('change', updateCustomPreview);
            });

            addBtn.addEventListener('click', () => {
                let selectedToppings = [];
                let toppingTotal = 0;
                toppings.forEach(top => {
                    if (top.checked) {
                        selectedToppings.push(top.getAttribute('data-name'));
                        toppingTotal += parseInt(top.getAttribute('data-price'));
                    }
                });

                const customItem = {
                    id: Date.now(),
                    name: `AREPA CREADA: ${currentBase.name}`,
                    price: currentBase.price + toppingTotal,
                    quantity: 1,
                    description: selectedToppings.join(', ')
                };

                cart.push(customItem);
                updateCartUI();
                showToast("¡AREPA PERSONALIZADA AGREGADA!");
            });

            updateCustomPreview();
        }

        function sendWhatsAppOrder() {
            if (cart.length === 0) {
                showToast("TU CARRITO ESTÁ VACÍO");
                return;
            }

            let message = "¡Hola *CAFEPA Colombia*! ☕🫓 Quisiera realizar el siguiente pedido:\n\n";
            cart.forEach(item => {
                message += `• *${item.quantity}x* ${item.name} - ${formatCOP(item.price * item.quantity)}\n`;
            });

            const total = cart.reduce((acc, curr) => acc + (curr.price * curr.quantity), 0);
            message += `\n💰 *Total a pagar:* ${formatCOP(total)}`;
            message += "\n\nPor favor confirmar tiempo de despacho e instrucciones de pago. ¡Gracias!";

            const encodedMessage = encodeURIComponent(message);
            const phoneNumber = "573001234567";
            window.open(`https://wa.me/${phoneNumber}?text=${encodedMessage}`, '_blank');
        }

        function showToast(message) {
            const toast = document.getElementById('toast');
            const toastMsg = document.getElementById('toastMsg');
            toastMsg.textContent = message;

            toast.classList.remove('translate-y-20', 'opacity-0');
            setTimeout(() => {
                toast.classList.add('translate-y-20', 'opacity-0');
            }, 3000);
        }
    </script>
</body>
</html>