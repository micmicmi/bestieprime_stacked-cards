
        gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);

        function initExpertiseScrollEffect() {
            const section = document.querySelector('.mwg_effect031');
            const slides = gsap.utils.toArray('.mwg_effect031 .expertise-slide');
            const dots = document.querySelectorAll('.card-pagination .dot');

            // Set initial state
            slides.forEach((slide, i) => {
                gsap.set(slide, { zIndex: i });

                const mediaSide = slide.querySelector('.card-media-side');
                const textSide = slide.querySelector('.card-text-side');

                if (i > 0) {
                    gsap.set(mediaSide, { y: '100vh' });
                    gsap.set(textSide, { autoAlpha: 0, y: 15 });
                } else {
                    gsap.set(mediaSide, { y: 0 });
                    gsap.set(textSide, { autoAlpha: 1, y: 0 });
                }
            });

            const scrollDistance = slides.length * 550;

            const tl = gsap.timeline({
                paused: true
            });

            slides.forEach((slide, index) => {
                if (index < slides.length - 1) {
                    const nextSlide = slides[index + 1];

                    const currentMedia = slide.querySelector('.card-media-side');
                    const nextMedia = nextSlide.querySelector('.card-media-side');
                    const currentText = slide.querySelector('.card-text-side');
                    const nextText = nextSlide.querySelector('.card-text-side');

                    const stepLabel = 'step' + index;
                    tl.add(stepLabel);

                    tl.to(currentMedia, {
                        rotationZ: (Math.random() - 0.5) * 10,
                        scale: 0.7,
                        rotationX: 40,
                        autoAlpha: 0,
                        ease: 'power1.in',
                        duration: 1
                    }, stepLabel);

                    tl.to(nextMedia, {
                        y: '0%',
                        ease: 'none',
                        duration: 1
                    }, stepLabel);

                    tl.to(currentText, {
                        autoAlpha: 0,
                        y: -15,
                        ease: 'power1.inOut',
                        duration: 0.5
                    }, stepLabel);

                    tl.to(nextText, {
                        autoAlpha: 1,
                        y: 0,
                        ease: 'power1.inOut',
                        duration: 0.5
                    }, stepLabel + "+=0.5");
                }
            });

            let isActive = false;
            let currentTargetProgress = 0;

            section.addEventListener('mouseenter', () => { isActive = true; });
            section.addEventListener('mouseleave', () => { isActive = false; });

            document.addEventListener('click', (e) => {
                if (!section.contains(e.target)) {
                    isActive = false;
                } else {
                    isActive = true;
                }
            });

            function updateDots() {
                const progress = tl.progress();
                const activeIndex = Math.round(progress * (slides.length - 1));
                dots.forEach((dot, i) => {
                    dot.classList.toggle('active', i === activeIndex);
                });
            }

            section.addEventListener('wheel', (e) => {
                if (!isActive || window.innerWidth < 1024) return;

                const progress = tl.progress();

                if (e.deltaY < 0 && progress <= 0) return;
                if (e.deltaY > 0 && progress >= 1) return;

                e.preventDefault();

                const deltaProgress = e.deltaY / scrollDistance;
                currentTargetProgress += deltaProgress;
                currentTargetProgress = Math.max(0, Math.min(1, currentTargetProgress));

                gsap.to(tl, {
                    progress: currentTargetProgress,
                    duration: 0.5,
                    ease: "power2.out",
                    onUpdate: updateDots
                });
            }, { passive: false });

            dots.forEach((dot, i) => {
                dot.addEventListener('click', () => {
                    if (window.innerWidth < 1024) return;

                    const targetProgress = i / (slides.length - 1);
                    currentTargetProgress = targetProgress;

                    gsap.to(tl, {
                        progress: targetProgress,
                        duration: 0.8,
                        ease: 'power2.inOut',
                        onUpdate: updateDots
                    });
                });
            });
        }

        window.addEventListener("load", () => {
            if ('requestIdleCallback' in window) {
                requestIdleCallback(initExpertiseScrollEffect);
            } else {
                setTimeout(initExpertiseScrollEffect, 500);
            }
        });


        // --- Mobile Gallery Logic ---
        const mobileGallery = document.getElementById('mobileGallery');
        const mDots = document.querySelectorAll('.m-dot');
        const mStepNum = document.getElementById('m-step-num');
        const mStepHead = document.getElementById('m-step-head');
        const mStepBody = document.getElementById('m-step-body');

        const mobileStepsData = [
            {
                num: "01",
                head: "כמה הבית באמת עולה לכם?",
                body: "הגדרת מחיר הנכס וההון העצמי הם הבסיס לכל התהליך. נתונים אלה מאפשרים לנו לחשב את אחוז המימון המדויק."
            },
            {
                num: "02",
                head: "מה לגבי ההוצאות הנוספות?",
                body: "עורך דין, שמאי, תיווך ומס רכישה – אלו עלויות שיכולות להגיע לעשרות אלפי שקלים. אנחנו מחשבים עבורכם את הכל מראש."
            },
            {
                num: "03",
                head: "הפרופיל הפיננסי שלכם.",
                body: "נתוני השכר והיציבות התעסוקתית הם המפתח לקבלת ריביות מעולות. ככל שהמידע שתזינו יהיה מדויק יותר, כך נוכל להילחם עבורכם."
            },
            {
                num: "04",
                head: "כמה נוח לכם לשלם בחודש?",
                body: "אנחנו מתאימים את המשכנתא לחיים שלכם, לא להיפך. הגדרת החזר חודשי ריאלי תבטיח שתעמדו בתשלומים בנוחות."
            },
            {
                num: "05",
                head: "המשכנתא המנצחת מוכנה!",
                body: "המערכת מציגה לכם  2-3 תמהילים אופטימליים לבחירה: מאוזן, יציב או חסכוני. לכל אחד יתרונות משלו."
            }
        ];

        let currentActiveIndex = 0;

        if (mobileGallery) {
            mobileGallery.addEventListener('scroll', () => {
                const cards = mobileGallery.querySelectorAll('.mobile-card-item');
                let minDiff = Infinity;
                let activeIdx = 0;

                cards.forEach((card, i) => {
                    const cardRect = card.getBoundingClientRect();
                    const containerRect = mobileGallery.getBoundingClientRect();
                    const cardCenter = cardRect.left + cardRect.width / 2;
                    const containerCenter = containerRect.left + containerRect.width / 2;
                    const diff = Math.abs(cardCenter - containerCenter);

                    if (diff < minDiff) {
                        minDiff = diff;
                        activeIdx = i;
                    }
                });

                if (activeIdx !== currentActiveIndex) {
                    currentActiveIndex = activeIdx;
                    updateMobileText(activeIdx);
                }
            });

            // Mobile dot navigation
            mDots.forEach((dot, index) => {
                dot.addEventListener('click', () => {
                    const cards = mobileGallery.querySelectorAll('.mobile-card-item');
                    const targetCard = cards[index];
                    if (targetCard) {
                        mobileGallery.scrollTo({
                            left: targetCard.offsetLeft - 24, // Adjust for padding
                            behavior: 'smooth'
                        });
                    }
                });
            });
        }

        function updateMobileText(index) {
            mDots.forEach((dot, i) => dot.classList.toggle('active', i === index));

            gsap.to([mStepNum, mStepHead, mStepBody], {
                opacity: 0,
                y: 10,
                duration: 0.2,
                onComplete: () => {
                    mStepNum.textContent = mobileStepsData[index].num;
                    mStepHead.textContent = mobileStepsData[index].head;
                    mStepBody.textContent = mobileStepsData[index].body;
                    gsap.to([mStepNum, mStepHead, mStepBody], {
                        opacity: 1,
                        y: 0,
                        duration: 0.3
                    });
                }
            });
        }

        