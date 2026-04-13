# Example: Diffusion VLM Integration / 示例：扩散VLM对比方法集成

## Scenario
User goal: integrate several comparison methods into a diffusion VLM and produce weekly progress.

## Strategic Goal
Deliver a reproducible comparison pipeline with at least one stable baseline and one integrated comparison method.

## Primary Contradiction
Current bottleneck is not model quality; it is missing a minimal runnable baseline with reliable logging.

## Campaign Objective (This Week)
- Build a stable baseline run on a small subset.
- Integrate one comparison component only.
- Produce one measurable result table.

## Immediate Attack Tasks
1. Run baseline on 20 samples and archive logs.
2. Reproduce one known failure with full traceback.
3. Integrate component A behind a feature flag.
4. Run A/B comparison on fixed seed.

## Verification
- Baseline run completes without crash.
- Logs include timing + key metrics.
- Feature-flag switch works.
- A/B output table is generated.

## Pivot Conditions
- If same blocker appears in two routes, stop forcing full integration.
- Switch to local reproduction harness and isolate the failing boundary.

## Review Pattern
- Fact: what happened in this block?
- Diagnosis: bottleneck changed or unchanged?
- Next move: smallest startable action in next 15–30 minutes.
