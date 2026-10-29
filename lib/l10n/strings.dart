import 'package:flutter/widgets.dart';

import '../app_state.dart';
import '../config.dart';
import '../models/content.dart';

/// Interface text. English and Hindi sit side by side so a reviewer can check
/// both translations together.
class S {
  const S(this.lang);

  final AppLanguage lang;

  static S of(BuildContext context) => S(AppScope.of(context).language);

  String _t(String en, String hi) => lang == AppLanguage.hi ? hi : en;

  // App and navigation
  String get appName => _t('UPTET Saathi', 'UPTET साथी');
  String get navHome => _t('Home', 'होम');
  String get navPapers => _t('Papers', 'प्रश्नपत्र');
  String get navPractice => _t('Practice', 'अभ्यास');
  String get navProgress => _t('Progress', 'प्रगति');
  String get previousPapers => _t('Previous Papers', 'पिछले प्रश्नपत्र');
  String get practiceAndRevision => _t('Practice & Revision', 'अभ्यास और पुनरावृत्ति');
  String get myProgress => _t('My Progress', 'मेरी प्रगति');
  String get settings => _t('Settings', 'सेटिंग्स');
  String get language => _t('Language', 'भाषा');
  String languageName(AppLanguage l) => l == AppLanguage.hi ? 'हिन्दी' : 'English';
  String get contentVersionLabel => _t('Content version', 'सामग्री संस्करण');
  String get sendFeedback => _t('Send feedback', 'सुझाव भेजें');
  String get feedbackHint => _t('Tell us what is working and what to improve. Opens a short form in your browser.',
      'बताइए क्या अच्छा है और क्या सुधारना है। आपके ब्राउज़र में एक छोटा फ़ॉर्म खुलेगा।');
  String get reportProblem => _t('Report a problem with this question', 'इस प्रश्न में त्रुटि बताएँ');
  String get feedbackOpenFailed =>
      _t('The feedback form could not be opened. Please check your internet connection.',
          'सुझाव फ़ॉर्म नहीं खुल सका। कृपया अपना इंटरनेट कनेक्शन जाँचें।');

  // First launch, shown before a language is chosen, so always bilingual.
  static const chooseLanguageTitle = 'अपनी भाषा चुनें\nChoose your language';
  static const chooseLanguageHint = 'आप इसे बाद में बदल सकते हैं।\nYou can change this later.';

  // Shared
  String get ok => _t('OK', 'ठीक है');
  String get cancel => _t('Cancel', 'रद्द करें');
  String get tryAgain => _t('Try again', 'फिर से प्रयास करें');
  String get loadFailed =>
      _t('Something went wrong while loading. Please try again.', 'लोड करते समय समस्या हुई। कृपया फिर से प्रयास करें।');
  String questionsCount(int n) => _t(n == 1 ? '1 question' : '$n questions', '$n प्रश्न');
  String questionXofY(int x, int y) => _t('Question $x of $y', 'प्रश्न $x / $y');
  String get notVerified => _t('Not verified', 'असत्यापित');
  String get translationMissing => _t('English version not available — showing Hindi.',
      'हिन्दी संस्करण उपलब्ध नहीं — अंग्रेज़ी में दिखाया जा रहा है।');
  String get pilotNotice => _t('Pilot version: questions marked "Not verified" are still awaiting review.',
      'पायलट संस्करण: "असत्यापित" चिह्नित प्रश्नों की जाँच अभी बाकी है।');
  String get contentUpdateFailed => _t(
      'New study content could not be installed, so the previous content is being used.',
      'नई अध्ययन सामग्री इंस्टॉल नहीं हो सकी, इसलिए पिछली सामग्री का उपयोग हो रहा है।');

  // Home
  String get welcomeTitle => _t('Namaskar,', 'नमस्कार,');
  String get welcomeMessage => _t('Even a few minutes of practice today moves your preparation forward.',
      'आज कुछ मिनट का अभ्यास भी आपकी तैयारी को आगे बढ़ाता है।');
  String get continueWhereLeft => _t('Continue where you left off', 'जहाँ छोड़ा था, वहीं से जारी रखें');
  String get resume => _t('Resume', 'जारी रखें');
  String get revision => _t('Revision', 'पुनरावृत्ति');
  String dueTodayCount(int n) =>
      _t(n == 1 ? '1 question is due for revision today' : '$n questions are due for revision today',
          'आज $n प्रश्न दोहराने हैं');
  String get noneDueToday => _t('Nothing is due today.', 'आज दोहराने के लिए कुछ नहीं है।');
  String nextReviewOn(String date) => _t('Next review: $date', 'अगली पुनरावृत्ति: $date');
  String get revisionEmptyHint => _t('Questions you get wrong in a test will appear here for revision.',
      'टेस्ट में गलत हुए प्रश्न यहाँ पुनरावृत्ति के लिए आएँगे।');
  String get reviseNow => _t('Revise now', 'अभी दोहराएँ');
  String get startStudying => _t('Start studying', 'पढ़ाई शुरू करें');
  String get papersSubtitle => _t('Attempt a full paper', 'पूरा प्रश्नपत्र हल करें');
  String get practiceSubtitle => _t('Topic-wise practice', 'विषयवार अभ्यास');
  String get syllabus => _t('Syllabus', 'पाठ्यक्रम');
  String get syllabusSubtitle => _t('Exam pattern & syllabus', 'परीक्षा पैटर्न और पाठ्यक्रम');
  String get aboutUs => _t('About Us', 'हमारे बारे में');
  String get bannerDescription => _t(
      'Super TET test series from 21 November, with a detailed analysis after every test. Tap to join our WhatsApp group.',
      'Super TET टेस्ट सीरीज़ 21 नवंबर से, हर टेस्ट के बाद विस्तृत विश्लेषण। हमारे WhatsApp समूह से जुड़ने के लिए टैप करें।');
  String get whatsAppOpenFailed => _t('WhatsApp could not be opened. Please check your internet connection.',
      'WhatsApp नहीं खुल सका। कृपया अपना इंटरनेट कनेक्शन जाँचें।');
  String get progressSubtitle => _t('Scores, accuracy and weak topics', 'अंक, सटीकता और कमज़ोर विषय');

  // Papers
  String get noPapers => _t('No papers are available yet.', 'अभी कोई प्रश्नपत्र उपलब्ध नहीं है।');
  String get noPapersHint => _t('Papers appear here once they have been checked and added to the app.',
      'जाँच के बाद ऐप में जोड़े गए प्रश्नपत्र यहाँ दिखेंगे।');
  String examPapers(Exam exam) => switch (exam) {
        Exam.uptet => _t('UPTET previous papers', 'UPTET के पिछले प्रश्नपत्र'),
        Exam.ctet => _t('CTET previous papers', 'CTET के पिछले प्रश्नपत्र'),
      };
  String levelName(ExamLevel level) => switch (level) {
        ExamLevel.primary => _t('Primary level · Classes I–V', 'प्राथमिक स्तर · कक्षा 1–5'),
        ExamLevel.junior => _t('Junior level · Classes VI–VIII', 'उच्च प्राथमिक (जूनियर) स्तर · कक्षा 6–8'),
      };
  String get practiceSets => _t('Practice sets', 'अभ्यास सेट');
  String get officialPaper => _t('Official previous-year paper', 'आधिकारिक पिछले वर्ष का प्रश्नपत्र');
  String get practiceSetBadge => _t('Practice set · not an official paper', 'अभ्यास सेट · आधिकारिक प्रश्नपत्र नहीं');
  String minutes(int n) => _t('$n min', '$n मिनट');
  String get yearLabel => _t('Year', 'वर्ष');
  String get paperCodeLabel => _t('Paper code', 'प्रश्नपत्र कोड');
  String get questionsLabel => _t('Questions', 'प्रश्न');
  String get durationLabel => _t('Suggested time', 'सुझाया गया समय');
  String get languagesLabel => _t('Languages', 'भाषाएँ');
  String get markingLabel => _t('Marking', 'अंकन');
  String marking(MarkingScheme m) {
    final correct = formatNumber(m.correct);
    if (m.incorrect == 0) {
      return _t('+$correct per correct answer, no negative marking', 'हर सही उत्तर पर +$correct, कोई ऋणात्मक अंकन नहीं');
    }
    final wrong = formatNumber(m.incorrect);
    return _t('+$correct per correct answer, $wrong per wrong answer', 'हर सही उत्तर पर +$correct, हर गलत उत्तर पर $wrong');
  }

  String get viewPdf => _t('View the original paper (PDF)', 'मूल प्रश्नपत्र देखें (PDF)');
  String get pdfFailed => _t('The PDF could not be opened.', 'PDF नहीं खुल सका।');
  String pageXofY(int x, int y) => _t('Page $x of $y', 'पृष्ठ $x / $y');
  String get startTest => _t('Start test', 'टेस्ट शुरू करें');
  String get startAgain => _t('Start again', 'फिर से शुरू करें');
  String get startAgainTitle => _t('Start again?', 'फिर से शुरू करें?');
  String get startAgainBody => _t(
      'Your unfinished answers will be cleared. Results of completed tests are not affected.',
      'आपके अधूरे उत्तर हट जाएँगे। पूरे किए गए टेस्ट के परिणाम सुरक्षित रहेंगे।');
  String get noQuestionsAvailable => _t('No questions are available for this yet.', 'इसके लिए अभी कोई प्रश्न उपलब्ध नहीं है।');
  String get yourAttempts => _t('Your attempts', 'आपके प्रयास');

  // Test settings
  String get testSettings => _t('Test settings', 'टेस्ट सेटिंग्स');
  String get modePractice => _t('Practice', 'अभ्यास');
  String get modeMock => _t('Mock test', 'मॉक टेस्ट');
  String get practiceModeHint => _t('No timer: take as long as you need.', 'कोई टाइमर नहीं: जितना समय चाहिए, लें।');
  String get mockModeHint => _t(
      'Timed like the real exam. The test is submitted automatically when time runs out. The timer pauses while you are away from the test.',
      'असली परीक्षा की तरह समयबद्ध। समय समाप्त होने पर टेस्ट अपने आप जमा हो जाता है। टेस्ट से बाहर रहने पर टाइमर रुका रहता है।');
  String fullTime(int minutes) => _t('Full time · $minutes min', 'पूरा समय · $minutes मिनट');
  String get shuffleQuestions => _t('Shuffle question order', 'प्रश्नों का क्रम बदलें');
  String get timeLeft => _t('Time left', 'शेष समय');
  String get timeUp => _t('Time is up. Your test has been submitted.', 'समय समाप्त। आपका टेस्ट जमा कर दिया गया है।');
  String get timeTaken => _t('Time taken', 'लगा समय');
  String ofTimeLimit(String taken, int minutes) => _t('$taken of $minutes min', '$minutes मिनट में से $taken');
  String get mockLeaveBody => _t('Your answers are saved and the timer is paused. You can continue later from Home.',
      'आपके उत्तर सहेजे गए हैं और टाइमर रुका है। आप बाद में होम से जारी रख सकते हैं।');
  String get couldNotStart => _t('The test could not be started. Please try again.', 'टेस्ट शुरू नहीं हो सका। कृपया फिर से प्रयास करें।');

  // Quiz
  String get previous => _t('Previous', 'पिछला');
  String get next => _t('Next', 'अगला');
  String get submit => _t('Submit', 'जमा करें');
  String get submitTest => _t('Submit test', 'टेस्ट जमा करें');
  String get submitTitle => _t('Submit this test?', 'क्या यह टेस्ट जमा करें?');
  String submitBody(int answered, int unanswered) => _t(
      'Answered: $answered\nNot answered: $unanswered\n\nYou cannot change answers after submitting.',
      'उत्तर दिए: $answered\nउत्तर नहीं दिए: $unanswered\n\nजमा करने के बाद उत्तर बदले नहीं जा सकते।');
  String get leaveTitle => _t('Leave the test?', 'टेस्ट छोड़ें?');
  String get leaveBody => _t('Your answers are saved. You can continue later from Home.',
      'आपके उत्तर सहेजे गए हैं। आप बाद में होम से जारी रख सकते हैं।');
  String get leave => _t('Leave', 'छोड़ें');
  String get stay => _t('Stay', 'रुकें');
  String get allQuestions => _t('All questions', 'सभी प्रश्न');
  String get answered => _t('Answered', 'उत्तर दिया');
  String get answerSaveFailed =>
      _t('This answer could not be saved. Please select it again.', 'यह उत्तर सहेजा नहीं जा सका। कृपया फिर से चुनें।');
  String get submitFailed => _t('Your result could not be saved. Your answers are still here — please try again.',
      'आपका परिणाम सहेजा नहीं जा सका। आपके उत्तर यहीं हैं — कृपया फिर से प्रयास करें।');
  String get testUnavailable => _t('This test could not be opened.', 'यह टेस्ट खोला नहीं जा सका।');

  // Results
  String get result => _t('Result', 'परिणाम');
  String get score => _t('Score', 'अंक');
  String get correct => _t('Correct', 'सही');
  String get incorrect => _t('Incorrect', 'गलत');
  String get notAnswered => _t('Not answered', 'उत्तर नहीं दिया');
  String get accuracy => _t('Accuracy', 'सटीकता');
  String addedToRevision(int n) => _t(
      n == 1 ? '1 incorrect question was added to your revision list.' : '$n incorrect questions were added to your revision list.',
      '$n गलत प्रश्न आपकी पुनरावृत्ति सूची में जोड़े गए।');
  String submittedOn(String when) => _t('Submitted $when', 'जमा किया: $when');
  String get all => _t('All', 'सभी');
  String get yourAnswer => _t('Your answer', 'आपका उत्तर');
  String get correctAnswer => _t('Correct answer', 'सही उत्तर');
  String get explanation => _t('Explanation', 'व्याख्या');
  String get youDidNotAnswer => _t('You did not answer this question.', 'आपने इस प्रश्न का उत्तर नहीं दिया।');
  String get nothingInFilter => _t('No questions in this list.', 'इस सूची में कोई प्रश्न नहीं है।');
  String get done => _t('Done', 'हो गया');

  // Practice & revision
  String get topicPractice => _t('Topic-wise practice', 'विषयवार अभ्यास');
  String get noSubjects => _t('No subjects are available yet.', 'अभी कोई विषय उपलब्ध नहीं है।');
  String get noTopicQuestions => _t('No questions yet', 'अभी कोई प्रश्न नहीं');
  String get unfinishedPractice => _t('Unfinished practice', 'अधूरा अभ्यास');
  String stoppedAt(int x, int y) => _t('You stopped at question $x of $y.', 'आप प्रश्न $x / $y पर रुके थे।');
  String get revisionList => _t('Revision list', 'पुनरावृत्ति सूची');
  String get dueToday => _t('Due today', 'आज दोहराने हैं');
  String get upcoming => _t('Upcoming', 'आगामी');
  String get mastered => _t('Mastered', 'पक्के हो गए');
  String upcomingCount(int n) => _t('$n upcoming', '$n आगामी');
  String masteredCount(int n) => _t('$n mastered', '$n पक्के');
  String reviewStep(int stage, int total) => _t('Review ${stage + 1} of $total', 'पुनरावृत्ति ${stage + 1} / $total');
  String dueOn(String date) => _t('Due $date', 'तिथि: $date');
  String get revisionListEmpty => _t('Your revision list is empty.', 'आपकी पुनरावृत्ति सूची खाली है।');
  String get revisionSchedule {
    final steps = AppConfig.revisionIntervalsDays;
    final en = steps.map((d) => d == 1 ? 'the next day' : '$d days later').join(', then ');
    final hi = steps.map((d) => d == 1 ? 'अगले दिन' : '$d दिन बाद').join(', फिर ');
    return _t(
        'Wrong answers come back $en. Get a question right ${steps.length} times in a row and it is mastered.',
        'गलत उत्तर वाले प्रश्न $hi दोबारा आते हैं। लगातार ${steps.length} बार सही उत्तर देने पर प्रश्न पक्का हो जाता है।');
  }

  // Review session
  String get checkAnswer => _t('Check answer', 'उत्तर जाँचें');
  String get rightFeedback => _t('Correct!', 'सही उत्तर!');
  String get wrongFeedback => _t('Not quite.', 'यह उत्तर सही नहीं है।');
  String seeAgainIn(int days) => days == 1
      ? _t('You will see this question again tomorrow.', 'यह प्रश्न कल फिर आएगा।')
      : _t('You will see this question again in $days days.', 'यह प्रश्न $days दिन बाद फिर आएगा।');
  String get masteredFeedback => _t('Mastered! This question leaves your revision list.',
      'पक्का हो गया! यह प्रश्न अब पुनरावृत्ति सूची से हट गया।');
  String get finish => _t('Finish', 'समाप्त करें');
  String reviewSummary(int correct, int total) =>
      _t('You revised $total questions and got $correct right.', 'आपने $total प्रश्न दोहराए, जिनमें $correct सही रहे।');
  String get nothingDue => _t('Nothing is due for revision right now.', 'अभी दोहराने के लिए कुछ नहीं है।');
  String get reviewSaveFailed =>
      _t('This answer could not be saved. Please try again.', 'यह उत्तर सहेजा नहीं जा सका। कृपया फिर से प्रयास करें।');

  // Progress
  String get progressEmptyTitle => _t('No tests completed yet', 'अभी कोई टेस्ट पूरा नहीं हुआ');
  String get progressEmptyBody => _t('Finish a paper or a topic practice and your results will appear here.',
      'कोई प्रश्नपत्र या विषय अभ्यास पूरा करें, आपके परिणाम यहाँ दिखेंगे।');
  String get testsCompleted => _t('Tests completed', 'पूरे किए गए टेस्ट');
  String get questionsAttempted => _t('Questions attempted', 'हल किए गए प्रश्न');
  String get answeredCorrectly => _t('Answered correctly', 'सही उत्तर');
  String get answeredIncorrectly => _t('Answered incorrectly', 'गलत उत्तर');
  String get skipped => _t('Skipped', 'छोड़े गए');
  String get awaitingRevision => _t('Awaiting revision', 'पुनरावृत्ति बाकी');
  String get accuracyNote => _t('Accuracy counts only the questions you answered.', 'सटीकता केवल उत्तर दिए गए प्रश्नों पर गिनी जाती है।');
  String get topicsToPractise => _t('Topics to practise', 'अभ्यास की ज़रूरत वाले विषय');
  String notEnoughData(int min) => _t('A topic is judged once you have answered at least $min of its questions.',
      'किसी विषय के कम से कम $min प्रश्न हल करने पर ही उसका आकलन होता है।');
  String get noWeakTopics => _t('No weak topics right now. Keep practising!', 'अभी कोई कमज़ोर विषय नहीं। अभ्यास जारी रखें!');
  String get topicPerformance => _t('Topic performance', 'विषयवार प्रदर्शन');
  String topicStats(int correct, int answered) => _t('$correct of $answered correct', '$answered में से $correct सही');
  String get needsPractice => _t('Needs practice', 'अभ्यास चाहिए');
  String get history => _t('Test history', 'टेस्ट इतिहास');
  String get aboutDataTitle => _t('Your data', 'आपका डेटा');
  String get aboutDataBody => _t(
      'Stored only on this phone: your language, your answers and scores, and your revision schedule. '
          'There is no account and UPTET Saathi has no server, so we never receive your data. '
          'If you uninstall the app or lose this phone, your progress may not be recoverable. '
          'If you send feedback, only what you write in the form, and the ID of a question you report, reaches us.',
      'केवल इसी फ़ोन में सहेजा जाता है: आपकी भाषा, आपके उत्तर और अंक, और आपकी पुनरावृत्ति सूची। '
          'कोई खाता नहीं है और UPTET साथी का कोई सर्वर नहीं है, इसलिए आपका डेटा हमारे पास नहीं आता। '
          'ऐप हटाने (अनइंस्टॉल) या फ़ोन खो जाने पर आपकी प्रगति शायद वापस न मिल सके। '
          'सुझाव भेजने पर केवल फ़ॉर्म में लिखी आपकी बात और बताए गए प्रश्न की ID ही हम तक पहुँचती है।');

  // Papers list
  String paperCount(int n) => _t(n == 1 ? '1 paper' : '$n papers', '$n प्रश्नपत्र');
  String examName(Exam exam) => switch (exam) {
        Exam.uptet => 'UPTET',
        Exam.ctet => 'CTET',
      };
  String levelShort(ExamLevel level) => switch (level) {
        ExamLevel.primary => _t('Primary (Classes 1 to 5)', 'प्राथमिक (कक्षा 1 से 5)'),
        ExamLevel.junior => _t('Junior (Classes 6 to 8)', 'जूनियर (कक्षा 6 से 8)'),
      };
  String levelWord(ExamLevel level) => switch (level) {
        ExamLevel.primary => _t('Primary', 'प्राथमिक'),
        ExamLevel.junior => _t('Junior', 'जूनियर'),
      };
  String levelClasses(ExamLevel level) => switch (level) {
        ExamLevel.primary => _t('Classes 1–5', 'कक्षा 1–5'),
        ExamLevel.junior => _t('Classes 6–8', 'कक्षा 6–8'),
      };
  String get shareApp => _t('Share UPTET Saathi', 'UPTET साथी शेयर करें');
  String get shareAppSubtitle => _t('Invite friends preparing for UPTET', 'UPTET की तैयारी कर रहे साथियों को बुलाएँ');
  String shareMessage(String link) => _t(
      'Preparing for UPTET? Try UPTET Saathi: previous papers, topic-wise practice and revision in Hindi and English, even offline. $link',
      'UPTET की तैयारी कर रहे हैं? UPTET साथी आज़माएँ: पिछले प्रश्नपत्र, विषयवार अभ्यास और दोहराई, हिन्दी और अंग्रेज़ी में, बिना इंटरनेट के भी। $link');
  String get shareFailed => _t('Sharing could not be opened.', 'शेयर नहीं खुल सका।');
  String get downloadPaper => _t('Download Paper', 'प्रश्नपत्र डाउनलोड करें');
  String savedToDownloads(String name) => _t('Saved to Downloads: $name', 'डाउनलोड्स में सहेजा गया: $name');
  String get downloadFailed =>
      _t('The paper could not be saved. Please try again.', 'प्रश्नपत्र सहेजा नहीं जा सका। कृपया फिर से प्रयास करें।');
  String get storagePermissionNeeded => _t('Allow storage access to save the paper, then try again.',
      'प्रश्नपत्र सहेजने के लिए स्टोरेज की अनुमति दें, फिर से प्रयास करें।');
  String get openFullScreen => _t('Open full screen', 'पूरी स्क्रीन पर खोलें');

  // Practice
  String get topicWiseQuestions => _t('Topic-wise questions', 'प्रकरणवार प्रश्न');
  String get topicWiseSubtitle => _t('Practise by subject and topic', 'विषय और प्रकरण के अनुसार अभ्यास');
  String get subjectWiseQuestions => _t('Subject-wise questions', 'विषयवार प्रश्न');
  String get fullPracticeSet => _t('Full Practice Set', 'पूर्ण अभ्यास सेट');
  String get fullPracticeSubtitle => _t('Attempt a complete set', 'पूरा सेट हल करें');
  String get subjectPapersSubtitle => _t('Full papers with this subject', 'इस विषय वाले पूरे प्रश्नपत्र');
  String get noPracticeSets => _t('No practice sets are available yet.', 'अभी कोई अभ्यास सेट उपलब्ध नहीं है।');
  String get reviseMistakes => _t('Revise mistakes', 'गलतियाँ दोहराएँ');
  String get noTopicsYet => _t('No topics are available yet.', 'अभी कोई प्रकरण उपलब्ध नहीं है।');

  // Question screen
  String get skip => _t('Skip ›››', 'छोड़ें ›››');
  String get nextArrows => _t('Next ›››', 'अगला ›››');
  String get noExplanation =>
      _t('No explanation is available for this question yet.', 'इस प्रश्न की व्याख्या अभी उपलब्ध नहीं है।');

  // Progress page
  String outOf(int n) => _t('Out of $n', '$n में से');
  String get papersCompletedLabel => _t('Papers completed', 'पूरे किए गए प्रश्नपत्र');
  String get weeklyTime => _t('Time this week', 'इस सप्ताह का समय');
  String get questionReport => _t('Question report', 'प्रश्न रिपोर्ट');
  String dayStreak(int n) => _t(n == 1 ? '1-day streak' : '$n-day streak', 'लगातार $n दिन');
  String bestStreak(int n) => _t(n == 1 ? 'Best: 1 day' : 'Best: $n days', 'सर्वश्रेष्ठ: $n दिन');
  String get startStreak =>
      _t('Answer a question today to start your streak.', 'लगातार पढ़ाई शुरू करने के लिए आज एक प्रश्न हल करें।');
  String get keepStreak => _t('Study today to keep your streak going.', 'लगातार पढ़ाई बनाए रखने के लिए आज भी अभ्यास करें।');
  String get chooseMonth => _t('Choose month', 'महीना चुनें');
  String get less => _t('Less', 'कम');
  String get more => _t('More', 'ज़्यादा');

  /// Row labels of the heat map, Monday first; only every other day is named.
  List<String> get weekdayLabels =>
      lang == AppLanguage.hi ? const ['सोम', '', 'बुध', '', 'शुक्र', '', ''] : const ['Mon', '', 'Wed', '', 'Fri', '', ''];
  String monthShort(int month) => (lang == AppLanguage.hi
      ? const ['जन', 'फ़र', 'मार्च', 'अप्रै', 'मई', 'जून', 'जुला', 'अग', 'सित', 'अक्टू', 'नव', 'दिस']
      : const ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])[month - 1];
  String dayActivity(String date, int questions, String time) =>
      _t('$date: $questions questions, $time', '$date: $questions प्रश्न, $time');

  /// `45m`, `2h 30m`, or `14h` from ten hours up.
  String studyTime(Duration d) {
    final h = d.inHours, m = d.inMinutes.remainder(60);
    if (h == 0) return _t('${m}m', '$m मि');
    if (h >= 10 || m == 0) return _t('${h}h', '$h घं');
    return _t('${h}h ${m}m', '$h घं $m मि');
  }

  // Syllabus
  String get examPattern => _t('UPTET exam pattern', 'UPTET परीक्षा पैटर्न');
  String get paperOne => _t('Paper I · Primary (Classes 1 to 5)', 'प्रश्नपत्र I · प्राथमिक (कक्षा 1 से 5)');
  String get paperTwo => _t('Paper II · Junior (Classes 6 to 8)', 'प्रश्नपत्र II · जूनियर (कक्षा 6 से 8)');
  String get sectionCdp => _t('Child Development & Pedagogy', 'बाल विकास एवं शिक्षण विधि');
  String get sectionLanguageOne => _t('Language I (Hindi)', 'भाषा I (हिन्दी)');
  String get sectionLanguageTwo => _t('Language II (English, Urdu or Sanskrit)', 'भाषा II (अंग्रेज़ी, उर्दू या संस्कृत)');
  String get sectionMaths => _t('Mathematics', 'गणित');
  String get sectionEvs => _t('Environmental Studies', 'पर्यावरण अध्ययन');
  String get sectionMathsScienceOrSst => _t('Maths & Science, or Social Studies', 'गणित एवं विज्ञान, या सामाजिक अध्ययन');
  String questionsShort(int n) => _t('$n Q', '$n प्रश्न');
  String get patternTotals => _t('150 questions · 150 marks · 2½ hours', '150 प्रश्न · 150 अंक · 2½ घंटे');
  String get patternRules => _t(
      'Every question carries one mark and there is no negative marking. '
          'To qualify you need 60% (90 marks) in the general category and 55% in reserved categories.',
      'हर प्रश्न एक अंक का है और कोई ऋणात्मक अंकन नहीं है। '
          'उत्तीर्ण होने के लिए सामान्य वर्ग में 60% (90 अंक) और आरक्षित वर्गों में 55% अंक चाहिए।');
  String get patternNote =>
      _t('The pattern can change. Always check the latest official notification.', 'पैटर्न बदल सकता है। हमेशा नवीनतम आधिकारिक अधिसूचना देखें।');
  String get topicsInApp => _t('Topics you can practise here', 'यहाँ अभ्यास के लिए उपलब्ध प्रकरण');

  // About
  String get aboutBody => _t(
      'We are a team driven by the belief that quality education and the right guidance can help everyone achieve their dreams. '
          'We created UPTET Saathi to make exam preparation simpler, more accessible, and less stressful for aspiring teachers. '
          "We understand that managing studies alongside work and daily responsibilities isn't easy, "
          'so we wanted to build something that fits into everyday life.\n\n'
          'Our goal is to make learning more convenient through practice, revision, and accessible study resources in Hindi and English.\n\n'
          'We are continuously working to make UPTET Saathi a helpful companion for every aspirant on their journey to becoming a teacher.',
      'हम एक ऐसी टीम हैं जिसका विश्वास है कि अच्छी शिक्षा और सही मार्गदर्शन से हर कोई अपने सपने पूरे कर सकता है। '
          'हमने UPTET साथी इसलिए बनाया ताकि शिक्षक बनने की तैयारी कर रहे लोगों के लिए परीक्षा की तैयारी आसान, सुलभ और कम तनाव वाली हो। '
          'हम समझते हैं कि काम और रोज़ की ज़िम्मेदारियों के साथ पढ़ाई करना आसान नहीं है, '
          'इसलिए हम कुछ ऐसा बनाना चाहते थे जो रोज़मर्रा की ज़िंदगी में फिट हो जाए।\n\n'
          'हमारा लक्ष्य है अभ्यास, दोहराई और हिन्दी व अंग्रेज़ी में सुलभ अध्ययन सामग्री के ज़रिए पढ़ाई को और सुविधाजनक बनाना।\n\n'
          'हम UPTET साथी को शिक्षक बनने की यात्रा में हर अभ्यर्थी का मददगार साथी बनाने के लिए लगातार काम कर रहे हैं।');
  static const aboutTagline = 'UPTET Saathi — आपकी तैयारी, हमारा साथ।';
  String get teamPhoto => _t('The UPTET Saathi team', 'UPTET साथी की टीम');
}

/// `2` for whole numbers, `0.25` otherwise.
String formatNumber(double value) {
  if (value == value.roundToDouble()) return value.toInt().toString();
  return value.toStringAsFixed(2).replaceFirst(RegExp(r'0+$'), '');
}
