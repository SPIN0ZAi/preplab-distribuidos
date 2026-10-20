# SDD Quickstart: 009-interaction-polish-and-motion

## 1. Using Motion Utility Classes

### Hover Lift on Venus Cards
To add an Apple-fluid hover lift with subtle shadow expansion:
```html
<div class="venus-card hover-lift">
  <!-- Card content -->
</div>
```

### Tactile Press on Controls
To provide tactile scale feedback on click:
```html
<button class="venus-button press-tactile">
  <!-- Button content -->
</button>
```

### Passing Exam Celebration
To trigger celebratory animation on passing score card:
```html
<div class="results-hero-card celebrate-pass">
  <!-- Score & badge content -->
</div>
```

## 2. Using CSS Motion Variables
```css
.custom-card {
  transition: transform var(--motion-duration-normal) var(--motion-ease-spring),
              box-shadow var(--motion-duration-normal) var(--motion-ease-spring);
}

@media (hover: hover) and (pointer: fine) {
  .custom-card:hover {
    transform: translateY(var(--motion-lift-y));
    box-shadow: var(--venus-shadow-hover);
  }
}
```
