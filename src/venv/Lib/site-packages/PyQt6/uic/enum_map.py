# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


# Map enum member names to fully scoped names.
EnumMap = {
    'Qt::AlignHCenter':         'Qt::Alignment::AlignHCenter',
    'Qt::AlignJustify':         'Qt::Alignment::AlignJustify',
    'Qt::AlignLeft':            'Qt::Alignment::AlignLeft',
    'Qt::AlignRight':           'Qt::Alignment::AlignRight',

    'Qt::AlignBaseline':        'Qt::Alignment::AlignBaseline',
    'Qt::AlignBottom':          'Qt::Alignment::AlignBottom',
    'Qt::AlignTop':             'Qt::Alignment::AlignTop',
    'Qt::AlignVCenter':         'Qt::Alignment::AlignVCenter',

    'Qt::AlignAbsolute':        'Qt::Alignment::AlignAbsolute',
    'Qt::AlignLeading':         'Qt::Alignment::AlignLeading',
    'Qt::AlignTrailing':        'Qt::Alignment::AlignTrailing',

    'Qt::AlignCenter':          'Qt::Alignment::AlignCenter',

    'Qt::AlignHorizontal_Mask': 'Qt::Alignment::AlignHorizontal_Mask',
    'Qt::AlignVertical_Mask':   'Qt::Alignment::AlignVertical_Mask',

    'Qt::DownArrow':    'Qt::ArrowType::DownArrow',
    'Qt::LeftArrow':    'Qt::ArrowType::LeftArrow',
    'Qt::NoArrow':      'Qt::ArrowType::NoArrow',
    'Qt::RightArrow':   'Qt::ArrowType::RightArrow',
    'Qt::UpArrow':      'Qt::ArrowType::UpArrow',

    'Qt::Checked':          'Qt::CheckState::Checked',
    'Qt::PartiallyChecked': 'Qt::CheckState::PartiallyChecked',
    'Qt::Unchecked':        'Qt::CheckState::Unchecked',

    'Qt::ActionsContextMenu':   'Qt::ContextMenuPolicy::ActionsContextMenu',
    'Qt::CustomContextMenu':    'Qt::ContextMenuPolicy::CustomContextMenu',
    'Qt::DefaultContextMenu':   'Qt::ContextMenuPolicy::DefaultContextMenu',
    'Qt::NoContextMenu':        'Qt::ContextMenuPolicy::NoContextMenu',
    'Qt::PreventContextMenu':   'Qt::ContextMenuPolicy::PreventContextMenu',

    'Qt::LogicalMoveStyle': 'Qt::CursorMoveStyle::LogicalMoveStyle',
    'Qt::VisualMoveStyle':  'Qt::CursorMoveStyle::VisualMoveStyle',

    'Qt::Monday':       'Qt::DayOfWeek::Monday',
    'Qt::Tuesday':      'Qt::DayOfWeek::Tuesday',
    'Qt::Wednesday':    'Qt::DayOfWeek::Wednesday',
    'Qt::Thursday':     'Qt::DayOfWeek::Thursday',
    'Qt::Friday':       'Qt::DayOfWeek::Friday',
    'Qt::Saturday':     'Qt::DayOfWeek::Saturday',
    'Qt::Sunday':       'Qt::DayOfWeek::Sunday',

    'Qt::AllDockWidgetAreas':   'Qt::DockWidgetAreas::AllDockWidgetAreas',
    'Qt::LeftDockWidgetArea':   'Qt::DockWidgetAreas::LeftDockWidgetArea',
    'Qt::RightDockWidgetArea':  'Qt::DockWidgetAreas::RightDockWidgetArea',
    'Qt::TopDockWidgetArea':    'Qt::DockWidgetAreas::TopDockWidgetArea',
    'Qt::BottomDockWidgetArea': 'Qt::DockWidgetAreas::BottomDockWidgetArea',
    'Qt::NoDockWidgetArea':     'Qt::DockWidgetAreas::NoDockWidgetArea',

    'Qt::ActionMask':       'Qt::DropActions::ActionMask',
    'Qt::CopyAction':       'Qt::DropActions::CopyAction',
    'Qt::IgnoreAction':     'Qt::DropActions::IgnoreAction',
    'Qt::LinkAction':       'Qt::DropActions::LinkAction',
    'Qt::MoveAction':       'Qt::DropActions::MoveAction',
    'Qt::TargetMoveAction': 'Qt::DropActions::TargetMoveAction',

    'Qt::ClickFocus':   'Qt::FocusPolicy::ClickFocus',
    'Qt::NoFocus':      'Qt::FocusPolicy::NoFocus',
    'Qt::TabFocus':     'Qt::FocusPolicy::TabFocus',
    'Qt::StrongFocus':  'Qt::FocusPolicy::StrongFocus',
    'Qt::WheelFocus':   'Qt::FocusPolicy::WheelFocus',

    'Qt::ImhDate':                  'Qt::InputMethodHints::ImhDate',
    'Qt::ImhDialableCharactersOnly':    'Qt::InputMethodHints::ImhDialableCharactersOnly',
    'Qt::ImhDigitsOnly':            'Qt::InputMethodHints::ImhDigitsOnly',
    'Qt::ImhEmailCharactersOnly':   'Qt::InputMethodHints::ImhEmailCharactersOnly',
    'Qt::ImhExclusiveInputMask':    'Qt::InputMethodHints::ImhExclusiveInputMask',
    'Qt::ImhFormattedNumbersOnly':  'Qt::InputMethodHints::ImhFormattedNumbersOnly',
    'Qt::ImhHiddenText':            'Qt::InputMethodHints::ImhHiddenText',
    'Qt::ImhLatinOnly':             'Qt::InputMethodHints::ImhLatinOnly',
    'Qt::ImhLowercaseOnly':         'Qt::InputMethodHints::ImhLowercaseOnly',
    'Qt::ImhMultiLine':             'Qt::InputMethodHints::ImhMultiLine',
    'Qt::ImhNoAutoUppercase':       'Qt::InputMethodHints::ImhNoAutoUppercase',
    'Qt::ImhNoEditMenu':            'Qt::InputMethodHints::ImhNoEditMenu',
    'Qt::ImhNoPredictiveText':      'Qt::InputMethodHints::ImhNoPredictiveText',
    'Qt::ImhNoTextHandles':         'Qt::InputMethodHints::ImhNoTextHandles',
    'Qt::ImhNone':                  'Qt::InputMethodHints::ImhNone',
    'Qt::ImhPreferLatin':           'Qt::InputMethodHints::ImhPreferLatin',
    'Qt::ImhPreferLowercase':       'Qt::InputMethodHints::ImhPreferLowercase',
    'Qt::ImhPreferNumbers':         'Qt::InputMethodHints::ImhPreferNumbers',
    'Qt::ImhPreferUppercase':       'Qt::InputMethodHints::ImhPreferUppercase',
    'Qt::ImhSensitiveData':         'Qt::InputMethodHints::ImhSensitiveData',
    'Qt::ImhTime':                  'Qt::InputMethodHints::ImhTime',
    'Qt::ImhUppercaseOnly':         'Qt::InputMethodHints::ImhUppercaseOnly',
    'Qt::ImhUrlCharactersOnly':     'Qt::InputMethodHints::ImhUrlCharactersOnly',

    'Qt::ItemIsAutoTristate':   'Qt::ItemFlags::ItemIsAutoTristate',
    'Qt::ItemIsDragEnabled':    'Qt::ItemFlags::ItemIsDragEnabled',
    'Qt::ItemIsDropEnabled':    'Qt::ItemFlags::ItemIsDropEnabled',
    'Qt::ItemIsEditable':       'Qt::ItemFlags::ItemIsEditable',
    'Qt::ItemIsEnabled':        'Qt::ItemFlags::ItemIsEnabled',
    'Qt::ItemIsSelectable':     'Qt::ItemFlags::ItemIsSelectable',
    'Qt::ItemIsUserCheckable':  'Qt::ItemFlags::ItemIsUserCheckable',
    'Qt::ItemIsUserTristate':   'Qt::ItemFlags::ItemIsUserTristate',
    'Qt::ItemNeverHasChildren': 'Qt::ItemFlags::ItemNeverHasChildren',
    'Qt::NoItemFlags':          'Qt::ItemFlags::NoItemFlags',

    'Qt::ContainsItemBoundingRect':     'Qt::ItemSelectionMode::ContainsItemBoundingRect',
    'Qt::ContainsItemShape':            'Qt::ItemSelectionMode::ContainsItemShape',
    'Qt::IntersectsItemBoundingRect':   'Qt::ItemSelectionMode::IntersectsItemBoundingRect',
    'Qt::IntersectsItemShape':          'Qt::ItemSelectionMode::IntersectsItemShape',

    'Qt::LayoutDirectionAuto':  'Qt::LayoutDirection::LayoutDirectionAuto',
    'Qt::LeftToRight':          'Qt::LayoutDirection::LeftToRight',
    'Qt::RightToLeft':          'Qt::LayoutDirection::RightToLeft',

    'Qt::Horizontal':   'Qt::Orientations::Horizontal',
    'Qt::Vertical':     'Qt::Orientations::Vertical',

    'Qt::CustomDashLine':   'Qt::PenStyle::CustomDashLine',
    'Qt::DashDotDotLine':   'Qt::PenStyle::DashDotDotLine',
    'Qt::DashDotLine':      'Qt::PenStyle::DashDotLine',
    'Qt::DashLine':         'Qt::PenStyle::DashLine',
    'Qt::DotLine':          'Qt::PenStyle::DotLine',
    'Qt::NoPen':            'Qt::PenStyle::NoPen',
    'Qt::SolidLine':        'Qt::PenStyle::SolidLine',

    'Qt::ScrollBarAlwaysOff':   'Qt::ScrollBarPolicy::ScrollBarAlwaysOff',
    'Qt::ScrollBarAlwaysOn':    'Qt::ScrollBarPolicy::ScrollBarAlwaysOn',
    'Qt::ScrollBarAsNeeded':    'Qt::ScrollBarPolicy::ScrollBarAsNeeded',

    'Qt::ElideLeft':    'Qt::TextElideMode::ElideLeft',
    'Qt::ElideRight':   'Qt::TextElideMode::ElideRight',
    'Qt::ElideMiddle':  'Qt::TextElideMode::ElideMiddle',
    'Qt::ElideNone':    'Qt::TextElideMode::ElideNone',

    'Qt::NoTextInteraction':            'Qt::TextInteractionFlags::NoTextInteraction',
    'Qt::TextSelectableByMouse':        'Qt::TextInteractionFlags::TextSelectableByMouse',
    'Qt::TextSelectableByKeyboard':     'Qt::TextInteractionFlags::TextSelectableByKeyboard',
    'Qt::LinksAccessibleByMouse':       'Qt::TextInteractionFlags::LinksAccessibleByMouse',
    'Qt::LinksAccessibleByKeyboard':    'Qt::TextInteractionFlags::LinksAccessibleByKeyboard',
    'Qt::TextEditable':                 'Qt::TextInteractionFlags::TextEditable',
    'Qt::TextEditorInteraction':        'Qt::TextInteractionFlags::TextEditorInteraction',
    'Qt::TextBrowserInteraction':       'Qt::TextInteractionFlags::TextBrowserInteraction',

    'Qt::AutoText':     'Qt::TextFormat::AutoText',
    'Qt::MarkdownText': 'Qt::TextFormat::MarkdownText',
    'Qt::PlainText':    'Qt::TextFormat::PlainText',
    'Qt::RichText':     'Qt::TextFormat::RichText',

    'Qt::LocalTime':        'Qt::TimeSpec::LocalTime',
    'Qt::OffsetFromUTC':    'Qt::TimeSpec::OffsetFromUTC',
    'Qt::TimeZone':         'Qt::TimeSpec::TimeZone',
    'Qt::UTC':              'Qt::TimeSpec::UTC',

    'Qt::LeftToolBarArea':      'Qt::ToolBarAreas::LeftToolBarArea',
    'Qt::RightToolBarArea':     'Qt::ToolBarAreas::RightToolBarArea',
    'Qt::TopToolBarArea':       'Qt::ToolBarAreas::TopToolBarArea',
    'Qt::BottomToolBarArea':    'Qt::ToolBarAreas::BottomToolBarArea',
    'Qt::AllToolBarAreas':      'Qt::ToolBarAreas::AllToolBarAreas',
    'Qt::NoToolBarArea':        'Qt::ToolBarAreas::NoToolBarArea',

    'Qt::ToolButtonFollowStyle':    'Qt::ToolButtonStyle::ToolButtonFollowStyle',
    'Qt::ToolButtonIconOnly':       'Qt::ToolButtonStyle::ToolButtonIconOnly',
    'Qt::ToolButtonTextBesideIcon': 'Qt::ToolButtonStyle::ToolButtonTextBesideIcon',
    'Qt::ToolButtonTextOnly':       'Qt::ToolButtonStyle::ToolButtonTextOnly',
    'Qt::ToolButtonTextUnderIcon':  'Qt::ToolButtonStyle::ToolButtonTextUnderIcon',

    'Qt::ApplicationModal': 'Qt::WindowModality::ApplicationModal',
    'Qt::NonModal':         'Qt::WindowModality::NonModal',
    'Qt::WindowModal':      'Qt::WindowModality::WindowModal',

    'QAbstractItemView::NoDragDrop':    'QAbstractItemView::DragDropMode::NoDragDrop',
    'QAbstractItemView::DragOnly':      'QAbstractItemView::DragDropMode::DragOnly',
    'QAbstractItemView::DropOnly':      'QAbstractItemView::DragDropMode::DropOnly',
    'QAbstractItemView::DragDrop':      'QAbstractItemView::DragDropMode::DragDrop',
    'QAbstractItemView::InternalMove':  'QAbstractItemView::DragDropMode::InternalMove',

    'QAbstractItemView::NoEditTriggers':    'QAbstractItemView::EditTriggers::NoEditTriggers',
    'QAbstractItemView::CurrentChanged':    'QAbstractItemView::EditTriggers::CurrentChanged',
    'QAbstractItemView::DoubleClicked':     'QAbstractItemView::EditTriggers::DoubleClicked',
    'QAbstractItemView::SelectedClicked':   'QAbstractItemView::EditTriggers::SelectedClicked',
    'QAbstractItemView::EditKeyPressed':    'QAbstractItemView::EditTriggers::EditKeyPressed',
    'QAbstractItemView::AnyKeyPressed':     'QAbstractItemView::EditTriggers::AnyKeyPressed',
    'QAbstractItemView::AllEditTriggers':   'QAbstractItemView::EditTriggers::AllEditTriggers',

    'QAbstractItemView::ScrollPerItem':     'QAbstractItemView::ScrollMode::ScrollPerItem',
    'QAbstractItemView::ScrollPerPixel':    'QAbstractItemView::ScrollMode::ScrollPerPixel',

    'QAbstractItemView::SelectColumns': 'QAbstractItemView::SelectionBehavior::SelectColumns',
    'QAbstractItemView::SelectItems':   'QAbstractItemView::SelectionBehavior::SelectItems',
    'QAbstractItemView::SelectRows':    'QAbstractItemView::SelectionBehavior::SelectRows',

    'QAbstractItemView::NoSelection':           'QAbstractItemView::SelectionMode::NoSelection',
    'QAbstractItemView::SingleSelection':       'QAbstractItemView::SelectionMode::SingleSelection',
    'QAbstractItemView::MultiSelection':        'QAbstractItemView::SelectionMode::MultiSelection',
    'QAbstractItemView::ExtendedSelection':     'QAbstractItemView::SelectionMode::ExtendedSelection',
    'QAbstractItemView::ContiguousSelection':   'QAbstractItemView::SelectionMode::ContiguousSelection',

    'QAbstractScrollArea::AdjustIgnored':               'QAbstractScrollArea::SizeAdjustPolicy::AdjustIgnored',
    'QAbstractScrollArea::AdjustToContents':            'QAbstractScrollArea::SizeAdjustPolicy::AdjustToContents',
    'QAbstractScrollArea::AdjustToContentsOnFirstShow': 'QAbstractScrollArea::SizeAdjustPolicy::AdjustToContentsOnFirstShow',

    'QAbstractSpinBox::NoButtons':      'QAbstractSpinBox::ButtonSymbols::NoButtons',
    'QAbstractSpinBox::PlusMinus':      'QAbstractSpinBox::ButtonSymbols::PlusMinus',
    'QAbstractSpinBox::UpDownArrows':   'QAbstractSpinBox::ButtonSymbols::UpDownArrows',

    'QAbstractSpinBox::CorrectToNearestValue': 'QAbstractSpinBox::CorrectionMode::CorrectToNearestValue',
    'QAbstractSpinBox::CorrectToPreviousValue': 'QAbstractSpinBox::CorrectionMode::CorrectToPreviousValue',

    'QAbstractSpinBox::AdaptiveDecimalStepType':    'QAbstractSpinBox::StepType::AdaptiveDecimalStepType',
    'QAbstractSpinBox::DefaultStepType':            'QAbstractSpinBox::StepType::DefaultStepType',

    'QCalendarWidget::LongDayNames':            'QCalendarWidget::HorizontalHeaderFormat::LongDayNames',
    'QCalendarWidget::NoHorizontalHeader':      'QCalendarWidget::HorizontalHeaderFormat::NoHorizontalHeader',
    'QCalendarWidget::ShortDayNames':           'QCalendarWidget::HorizontalHeaderFormat::ShortDayNames',
    'QCalendarWidget::SingleLetterDayNames':    'QCalendarWidget::HorizontalHeaderFormat::SingleLetterDayNames',

    'QCalendarWidget::NoSelection':     'QCalendarWidget::SelectionMode::NoSelection',
    'QCalendarWidget::SingleSelection': 'QCalendarWidget::SelectionMode::SingleSelection',

    'QCalendarWidget::ISOWeekNumbers':      'QCalendarWidget::VerticalHeaderFormat::ISOWeekNumbers',
    'QCalendarWidget::NoVerticalHeader':    'QCalendarWidget::VerticalHeaderFormat::NoVerticalHeader',

    'QComboBox::InsertAfterCurrent':    'QComboBox::InsertPolicy::InsertAfterCurrent',
    'QComboBox::InsertAlphabetically':  'QComboBox::InsertPolicy::InsertAlphabetically',
    'QComboBox::InsertAtBottom':        'QComboBox::InsertPolicy::InsertAtBottom',
    'QComboBox::InsertAtCurrent':       'QComboBox::InsertPolicy::InsertAtCurrent',
    'QComboBox::InsertAtTop':           'QComboBox::InsertPolicy::InsertAtTop',
    'QComboBox::InsertBeforeCurrent':   'QComboBox::InsertPolicy::InsertBeforeCurrent',
    'QComboBox::NoInsert':              'QComboBox::InsertPolicy::NoInsert',

    'QComboBox::AdjustToContents':                      'QComboBox::SizeAdjustPolicy::AdjustToContents',
    'QComboBox::AdjustToContentsOnFirstShow':           'QComboBox::SizeAdjustPolicy::AdjustToContentsOnFirstShow',
    'QComboBox::AdjustToMinimumContentsLengthWithIcon': 'QComboBox::SizeAdjustPolicy::AdjustToMinimumContentsLengthWithIcon',

    'QDateTimeEdit::NoSection':             'QDateTimeEdit::Sections::NoSection',
    'QDateTimeEdit::AmPmSection':           'QDateTimeEdit::Sections::AmPmSection',
    'QDateTimeEdit::MSecSection':           'QDateTimeEdit::Sections::MSecSection',
    'QDateTimeEdit::SecondSection':         'QDateTimeEdit::Sections::SecondSection',
    'QDateTimeEdit::MinuteSection':         'QDateTimeEdit::Sections::MinuteSection',
    'QDateTimeEdit::HourSection':           'QDateTimeEdit::Sections::HourSection',
    'QDateTimeEdit::DaySection':            'QDateTimeEdit::Sections::DaySection',
    'QDateTimeEdit::MonthSection':          'QDateTimeEdit::Sections::MonthSection',
    'QDateTimeEdit::YearSection':           'QDateTimeEdit::Sections::YearSection',

    'QDialogButtonBox::NoButton':           'QDialogButtonBox::StandardButtons::NoButton',
    'QDialogButtonBox::Ok':                 'QDialogButtonBox::StandardButtons::Ok',
    'QDialogButtonBox::Save':               'QDialogButtonBox::StandardButtons::Save',
    'QDialogButtonBox::SaveAll':            'QDialogButtonBox::StandardButtons::SaveAll',
    'QDialogButtonBox::Open':               'QDialogButtonBox::StandardButtons::Open',
    'QDialogButtonBox::Yes':                'QDialogButtonBox::StandardButtons::Yes',
    'QDialogButtonBox::YesToAll':           'QDialogButtonBox::StandardButtons::YesToAll',
    'QDialogButtonBox::No':                 'QDialogButtonBox::StandardButtons::No',
    'QDialogButtonBox::NoToAll':            'QDialogButtonBox::StandardButtons::NoToAll',
    'QDialogButtonBox::Abort':              'QDialogButtonBox::StandardButtons::Abort',
    'QDialogButtonBox::Retry':              'QDialogButtonBox::StandardButtons::Retry',
    'QDialogButtonBox::Ignore':             'QDialogButtonBox::StandardButtons::Ignore',
    'QDialogButtonBox::Close':              'QDialogButtonBox::StandardButtons::Close',
    'QDialogButtonBox::Cancel':             'QDialogButtonBox::StandardButtons::Cancel',
    'QDialogButtonBox::Discard':            'QDialogButtonBox::StandardButtons::Discard',
    'QDialogButtonBox::Help':               'QDialogButtonBox::StandardButtons::Help',
    'QDialogButtonBox::Apply':              'QDialogButtonBox::StandardButtons::Apply',
    'QDialogButtonBox::Reset':              'QDialogButtonBox::StandardButtons::Reset',
    'QDialogButtonBox::RestoreDefaults':    'QDialogButtonBox::StandardButtons::RestoreDefaults',

    'QDockWidget::DockWidgetClosable':          'QDockWidget::DockWidgetFeatures::DockWidgetClosable',
    'QDockWidget::DockWidgetFloatable':         'QDockWidget::DockWidgetFeatures::DockWidgetFloatable',
    'QDockWidget::DockWidgetMovable':           'QDockWidget::DockWidgetFeatures::DockWidgetMovable',
    'QDockWidget::DockWidgetVerticalTitleBar':  'QDockWidget::DockWidgetFeatures::DockWidgetVerticalTitleBar',
    'QDockWidget::NoDockWidgetFeatures':        'QDockWidget::DockWidgetFeatures::NoDockWidgetFeatures',

    'QFontComboBox::AllFonts':          'QFontComboBox::FontFilters::AllFonts',
    'QFontComboBox::MonospacedFonts':   'QFontComboBox::FontFilters::MonospacedFonts',
    'QFontComboBox::NonScalableFonts':  'QFontComboBox::FontFilters::NonScalableFonts',
    'QFontComboBox::ProportionalFonts': 'QFontComboBox::FontFilters::ProportionalFonts',
    'QFontComboBox::ScalableFonts':     'QFontComboBox::FontFilters::ScalableFonts',

    'QFontDatabase::Any':                   'QFontDatabase::WritingSystem::Any',
    'QFontDatabase::Latin':                 'QFontDatabase::WritingSystem::Latin',
    'QFontDatabase::Greek':                 'QFontDatabase::WritingSystem::Greek',
    'QFontDatabase::Cyrillic':              'QFontDatabase::WritingSystem::Cyrillic',
    'QFontDatabase::Armenian':              'QFontDatabase::WritingSystem::Armenian',
    'QFontDatabase::Hebrew':                'QFontDatabase::WritingSystem::Hebrew',
    'QFontDatabase::Arabic':                'QFontDatabase::WritingSystem::Arabic',
    'QFontDatabase::Syriac':                'QFontDatabase::WritingSystem::Syriac',
    'QFontDatabase::Thaana':                'QFontDatabase::WritingSystem::Thaana',
    'QFontDatabase::Devanagari':            'QFontDatabase::WritingSystem::Devanagari',
    'QFontDatabase::Bengali':               'QFontDatabase::WritingSystem::Bengali',
    'QFontDatabase::Gurmukhi':              'QFontDatabase::WritingSystem::Gurmukhi',
    'QFontDatabase::Gujarati':              'QFontDatabase::WritingSystem::Gujarati',
    'QFontDatabase::Oriya':                 'QFontDatabase::WritingSystem::Oriya',
    'QFontDatabase::Tamil':                 'QFontDatabase::WritingSystem::Tamil',
    'QFontDatabase::Telugu':                'QFontDatabase::WritingSystem::Telugu',
    'QFontDatabase::Kannada':               'QFontDatabase::WritingSystem::Kannada',
    'QFontDatabase::Malayalam':             'QFontDatabase::WritingSystem::Malayalam',
    'QFontDatabase::Sinhala':               'QFontDatabase::WritingSystem::Sinhala',
    'QFontDatabase::Thai':                  'QFontDatabase::WritingSystem::Thai',
    'QFontDatabase::Lao':                   'QFontDatabase::WritingSystem::Lao',
    'QFontDatabase::Tibetan':               'QFontDatabase::WritingSystem::Tibetan',
    'QFontDatabase::Myanmar':               'QFontDatabase::WritingSystem::Myanmar',
    'QFontDatabase::Georgian':              'QFontDatabase::WritingSystem::Georgian',
    'QFontDatabase::Khmer':                 'QFontDatabase::WritingSystem::Khmer',
    'QFontDatabase::SimplifiedChinese':     'QFontDatabase::WritingSystem::SimplifiedChinese',
    'QFontDatabase::TraditionalChinese':    'QFontDatabase::WritingSystem::TraditionalChinese',
    'QFontDatabase::Japanese':              'QFontDatabase::WritingSystem::Japanese',
    'QFontDatabase::Korean':                'QFontDatabase::WritingSystem::Korean',
    'QFontDatabase::Vietnamese':            'QFontDatabase::WritingSystem::Vietnamese',
    'QFontDatabase::Other':                 'QFontDatabase::WritingSystem::Other',
    'QFontDatabase::Symbol':                'QFontDatabase::WritingSystem::Symbol',
    'QFontDatabase::Ogham':                 'QFontDatabase::WritingSystem::Ogham',
    'QFontDatabase::Runic':                 'QFontDatabase::WritingSystem::Runic',
    'QFontDatabase::Nko':                   'QFontDatabase::WritingSystem::Nko',

    'QFrame::Box':          'QFrame::Shape::Box',
    'QFrame::HLine':        'QFrame::Shape::HLine',
    'QFrame::NoFrame':      'QFrame::Shape::NoFrame',
    'QFrame::Panel':        'QFrame::Shape::Panel',
    'QFrame::StyledPanel':  'QFrame::Shape::StyledPanel',
    'QFrame::VLine':        'QFrame::Shape::VLine',
    'QFrame::WinPanel':     'QFrame::Shape::WinPanel',

    'QFrame::Plain':    'QFrame::Shadow::Plain',
    'QFrame::Raised':   'QFrame::Shadow::Raised',
    'QFrame::Sunken':   'QFrame::Shadow::Sunken',

    'QGraphicsView::CacheNone':         'QGraphicsView::CacheMode::CacheNone',
    'QGraphicsView::CacheBackground':   'QGraphicsView::CacheMode::CacheBackground',

    'QGraphicsView::DontAdjustForAntialiasing': 'QGraphicsView::OptimizationFlags::DontAdjustForAntialiasing',
    'QGraphicsView::DontSavePainterState':      'QGraphicsView::OptimizationFlags::DontSavePainterState',

    'QGraphicsView::NoAnchor':          'QGraphicsView::ViewportAnchor::NoAnchor',
    'QGraphicsView::AnchorViewCenter':  'QGraphicsView::ViewportAnchor::AnchorViewCenter',
    'QGraphicsView::AnchorUnderMouse':  'QGraphicsView::ViewportAnchor::AnchorUnderMouse',

    'QGraphicsView::BoundingRectViewportUpdate':    'QGraphicsView::ViewportUpdateMode::BoundingRectViewportUpdate',
    'QGraphicsView::FullViewportUpdate':            'QGraphicsView::ViewportUpdateMode::FullViewportUpdate',
    'QGraphicsView::MinimalViewportUpdate':         'QGraphicsView::ViewportUpdateMode::MinimalViewportUpdate',
    'QGraphicsView::NoViewportUpdate':              'QGraphicsView::ViewportUpdateMode::NoViewportUpdate',
    'QGraphicsView::SmartViewportUpdate':           'QGraphicsView::ViewportUpdateMode::SmartViewportUpdate',

    'QLCDNumber::Bin':  'QLCDNumber::Mode::Bin',
    'QLCDNumber::Dec':  'QLCDNumber::Mode::Dec',
    'QLCDNumber::Hex':  'QLCDNumber::Mode::Hex',
    'QLCDNumber::Oct':  'QLCDNumber::Mode::Oct',

    'QLCDNumber::Filled':   'QLCDNumber::SegmentStyle::Filled',
    'QLCDNumber::Flat':     'QLCDNumber::SegmentStyle::Flat',
    'QLCDNumber::Outline':  'QLCDNumber::SegmentStyle::Outline',

    'QLineEdit::NoEcho':                'QLineEdit::EchoMode::NoEcho',
    'QLineEdit::Normal':                'QLineEdit::EchoMode::Normal',
    'QLineEdit::Password':              'QLineEdit::EchoMode::Password',
    'QLineEdit::PasswordEchoOnEdit':    'QLineEdit::EchoMode::PasswordEchoOnEdit',

    'QListView::LeftToRight':   'QListView::Flow::LeftToRight',
    'QListView::TopToBottom':   'QListView::Flow::TopToBottom',

    'QListView::Batched':       'QListView::LayoutMode::Batched',
    'QListView::SinglePass':    'QListView::LayoutMode::SinglePass',

    'QListView::Free':      'QListView::Movement::Free',
    'QListView::Snap':      'QListView::Movement::Snap',
    'QListView::Static':    'QListView::Movement::Static',

    'QListView::Adjust':    'QListView::ResizeMode::Adjust',
    'QListView::Fixed':     'QListView::ResizeMode::Fixed',

    'QListView::IconMode':  'QListView::ViewMode::IconMode',
    'QListView::ListMode':  'QListView::ViewMode::ListMode',

    'QMdiArea::SubWindowView':  'QMdiArea::ViewMode::SubWindowView',
    'QMdiArea::TabbedView':     'QMdiArea::ViewMode::TabbedView',

    'QMdiArea::ActivationHistoryOrder': 'QMdiArea::WindowOrder::ActivationHistoryOrder',
    'QMdiArea::CreationOrder':          'QMdiArea::WindowOrder::CreationOrder',
    'QMdiArea::StackingOrder':          'QMdiArea::WindowOrder::StackingOrder',

    'QPainter::Antialiasing':           'QPainter::RenderHints::Antialiasing',
    'QPainter::LosslessImageRendering': 'QPainter::RenderHints::LosslessImageRendering',
    'QPainter::SmoothPixmapTransform':  'QPainter::RenderHints::SmoothPixmapTransform',
    'QPainter::TextAntialiasing':       'QPainter::RenderHints::TextAntialiasing',

    'QPlainTextEdit::NoWrap':       'QPlainTextEdit::LineWrapMode::NoWrap',
    'QPlainTextEdit::WidgetWidth':  'QPlainTextEdit::LineWrapMode::WidgetWidth',

    'QProgressBar::BottomToTop':  'QProgressBar::Direction::BottomToTop',
    'QProgressBar::TopToBottom':  'QProgressBar::Direction::TopToBottom',

    'QQuickWidget::SizeRootObjectToView':   'QQuickWidget::ResizeMode::SizeRootObjectToView',
    'QQuickWidget::SizeViewToRootObject':   'QQuickWidget::ResizeMode::SizeViewToRootObject',

    'QSizePolicy::Fixed':               'QSizePolicy::Policy::Fixed',
    'QSizePolicy::Minimum':             'QSizePolicy::Policy::Minimum',
    'QSizePolicy::Maximum':             'QSizePolicy::Policy::Maximum',
    'QSizePolicy::Preferred':           'QSizePolicy::Policy::Preferred',
    'QSizePolicy::MinimumExpanding':    'QSizePolicy::Policy::MinimumExpanding',
    'QSizePolicy::Expanding':           'QSizePolicy::Policy::Expanding',
    'QSizePolicy::Ignored':             'QSizePolicy::Policy::Ignored',

    'QSlider::NoTicks':         'QSlider::TickPosition::NoTicks',
    'QSlider::TicksAbove':      'QSlider::TickPosition::TicksAbove',
    'QSlider::TicksBelow':      'QSlider::TickPosition::TicksBelow',
    'QSlider::TicksBothSides':  'QSlider::TickPosition::TicksBothSides',
    'QSlider::TicksLeft':       'QSlider::TickPosition::TicksLeft',
    'QSlider::TicksRight':      'QSlider::TickPosition::TicksRight',

    'QTabWidget::North':    'QTabWidget::TabPosition::North',
    'QTabWidget::South':    'QTabWidget::TabPosition::South',
    'QTabWidget::West':     'QTabWidget::TabPosition::West',
    'QTabWidget::East':     'QTabWidget::TabPosition::East',

    'QTabWidget::Rounded':      'QTabWidget::TabShape::Rounded',
    'QTabWidget::Triangular':   'QTabWidget::TabShape::Triangular',

    'QTextEdit::AutoAll':           'QTextEdit::AutoFormatting::AutoAll',
    'QTextEdit::AutoBulletList':    'QTextEdit::AutoFormatting::AutoBulletList',
    'QTextEdit::AutoNone':          'QTextEdit::AutoFormatting::AutoNone',

    'QTextEdit::FixedColumnWidth':  'QTextEdit::LineWrapMode::FixedColumnWidth',
    'QTextEdit::FixedPixelWidth':   'QTextEdit::LineWrapMode::FixedPixelWidth',
    'QTextEdit::NoWrap':            'QTextEdit::LineWrapMode::NoWrap',
    'QTextEdit::WidgetWidth':       'QTextEdit::LineWrapMode::WidgetWidth',

    'QToolButton::DelayedPopup':    'QToolButton::ToolButtonPopupMode::DelayedPopup',
    'QToolButton::InstantPopup':    'QToolButton::ToolButtonPopupMode::InstantPopup',
    'QToolButton::MenuButtonPopup': 'QToolButton::ToolButtonPopupMode::MenuButtonPopup',

    'QWizard::CancelButtonOnLeft':              'QWizard::WizardOptions::CancelButtonOnLeft',
    'QWizard::DisabledBackButtonOnLastPage':    'QWizard::WizardOptions::DisabledBackButtonOnLastPage',
    'QWizard::ExtendedWatermarkPixmap':         'QWizard::WizardOptions::ExtendedWatermarkPixmap',
    'QWizard::HaveCustomButton1':               'QWizard::WizardOptions::HaveCustomButton1',
    'QWizard::HaveCustomButton2':               'QWizard::WizardOptions::HaveCustomButton2',
    'QWizard::HaveCustomButton3':               'QWizard::WizardOptions::HaveCustomButton3',
    'QWizard::HaveFinishButtonOnEarlyPages':    'QWizard::WizardOptions::HaveFinishButtonOnEarlyPages',
    'QWizard::HaveHelpButton':                  'QWizard::WizardOptions::HaveHelpButton',
    'QWizard::HaveNextButtonOnLastPage':        'QWizard::WizardOptions::HaveNextButtonOnLastPage',
    'QWizard::HelpButtonOnRight':               'QWizard::WizardOptions::HelpButtonOnRight',
    'QWizard::IgnoreSubTitles':                 'QWizard::WizardOptions::IgnoreSubTitles',
    'QWizard::IndependentPages':                'QWizard::WizardOptions::IndependentPages',
    'QWizard::NoBackButtonOnLastPage':          'QWizard::WizardOptions::NoBackButtonOnLastPage',
    'QWizard::NoBackButtonOnStartPage':         'QWizard::WizardOptions::NoBackButtonOnStartPage',
    'QWizard::NoCancelButton':                  'QWizard::WizardOptions::NoCancelButton',
    'QWizard::NoCancelButtonOnLastPage':        'QWizard::WizardOptions::NoCancelButtonOnLastPage',
    'QWizard::NoDefaultButton':                 'QWizard::WizardOptions::NoDefaultButton',

    'QWizard::AeroStyle':       'QWizard::WizardStyle::AeroStyle',
    'QWizard::ClassicStyle':    'QWizard::WizardStyle::ClassicStyle',
    'QWizard::MacStyle':        'QWizard::WizardStyle::MacStyle',
    'QWizard::ModernStyle':     'QWizard::WizardStyle::ModernStyle',
}
