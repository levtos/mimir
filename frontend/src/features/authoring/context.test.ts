import { expect, it } from 'vitest';
import { newDefinition, newRule, ruleContext, withMinimumLanguage } from './model';

it('builds a typed origin condition and upgrades only the edited definition', () => {
  const original = newDefinition('example.input', 1);
  expect(withMinimumLanguage(original)).toBe(original);
  expect(original.language_version).toBeUndefined();
  const rule = newRule('known_automatic', ruleContext(original, false), { formulas: [], fusion: [], temporal: [] });
  expect(rule).toEqual({ op: 'known_automatic', arg: { op: 'input', name: 'a' } });
  const edited = withMinimumLanguage({ ...original, outputs: { value: rule } });
  expect(edited.language_version).toBe(3);
  expect(original.language_version).toBeUndefined();
});
