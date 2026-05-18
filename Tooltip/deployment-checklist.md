# tÅs Active Insights Deployment Checklist

## Pre-Deployment

- [ ] Confirm glossary terms are approved editorially.
- [ ] Confirm all source URLs are live.
- [ ] Confirm `active-insights-glossary.json` validates as JSON.
- [ ] Add CSS to site head.
- [ ] Add JS before closing body or via app template.
- [ ] Add `New here? Start simple.` button near top of the archive.
- [ ] Mark first-deployment terms manually with `data-tas-term`.

## Recommended First Terms

- [ ] `tas`
- [ ] `creative-intelligence`
- [ ] `creative-maverick`
- [ ] `scholar`
- [ ] `guide`
- [ ] `reflationary-lab`
- [ ] `reflectionary`
- [ ] `elevation-codex`
- [ ] `elevation-move`
- [ ] `somatic-tether`
- [ ] `steeping-as-time-design`
- [ ] `magnet`
- [ ] `symbol-a-ring`
- [ ] `calvin-mode`

## Functional QA

- [ ] Tooltips display on hover.
- [ ] Tooltips display on keyboard focus.
- [ ] Modals open on click.
- [ ] Modals open on Enter/Space.
- [ ] Escape closes modal.
- [ ] Close button works.
- [ ] Continue Reading links open in a new tab.
- [ ] Mobile tap works.
- [ ] Tooltip stays inside viewport.
- [ ] No console errors.

## Accessibility QA

- [ ] Keyboard-only flow works.
- [ ] Visible focus states are clear.
- [ ] Screen reader announces marked term as a button.
- [ ] Modal title is read when opened.
- [ ] Color contrast passes visual review.
- [ ] Reduced motion preference is respected.
- [ ] Site remains readable without JavaScript.

## Content QA

- [ ] Tooltip copy is one sentence.
- [ ] Expanded copy is clear and concise.
- [ ] Symbol explanations are optional, not mandatory.
- [ ] No term requires prior tÅs fluency.
- [ ] “Plain language first. Symbolic language second.” is honored.
- [ ] The page answers: What is this? Who is it for? What is offered?

## Vercel Deployment

- [ ] Commit files to repository.
- [ ] Confirm paths resolve after deployment.
- [ ] Preview deployment tested on desktop and mobile.
- [ ] Production deployment complete.
- [ ] Final smoke test performed on live URL.
