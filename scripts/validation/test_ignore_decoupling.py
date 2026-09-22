import unittest
import tempfile
import os
import shutil
import sys
import io
import contextlib

# Add repo root to sys.path so scripts can be imported
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.validation.image_links.image_links import (
    validate_missing,
    get_all_assets,
    main as image_links_main,
    IGNORE_CACHE,
    ASSET_IGNORE_CACHE,
)
from scripts.validation.relative_links.relative_links import (
    validate_file,
    map_file_to_url,
    build_route_map,
    is_ignored,
    main as relative_links_main,
    IGNORE_CACHE as REL_IGNORE_CACHE,
)


class TestImageLinksIgnoreDecoupling(unittest.TestCase):
    def setUp(self):
        IGNORE_CACHE.clear()
        ASSET_IGNORE_CACHE.clear()
        self.test_dir = tempfile.mkdtemp()
        self.content_dir = os.path.join(self.test_dir, 'content')
        os.makedirs(self.content_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        IGNORE_CACHE.clear()
        ASSET_IGNORE_CACHE.clear()

    def test_ignored_markdown_file_indexes_images_and_prevents_orphan_false_positive(self):
        """
        PAT-23 Part 1: If an ignored markdown file references an image in a shared
        non-ignored assets directory, that image must be added to referenced_images
        so get_all_assets() does not flag it as an orphaned unlinked asset.
        """
        # Create non-ignored assets directory with an image
        assets_dir = os.path.join(self.content_dir, 'shared', 'assets')
        os.makedirs(assets_dir)
        img_path = os.path.join(assets_dir, 'statusbar-terminal-hl.png')
        with open(img_path, 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n')

        # Create ignored subdirectory with a markdown file referencing the image
        ignored_sub = os.path.join(self.content_dir, 'software', 'app-lab', 'cli')
        os.makedirs(ignored_sub)
        with open(os.path.join(self.content_dir, 'software', 'app-lab', '.lintignore'), 'w') as f:
            f.write('cli/\n')

        md_file = os.path.join(ignored_sub, 'guide.md')
        rel_img = os.path.relpath(img_path, ignored_sub).replace('\\', '/')
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(f'# App Lab CLI\n\n![Screenshot]({rel_img})\n')

        # Validate
        missing, referenced = validate_missing(self.content_dir, self.test_dir, content_dir=self.content_dir)
        assets = get_all_assets(self.content_dir, self.test_dir)
        unlinked = assets - referenced

        self.assertIn(os.path.normpath(img_path), referenced)
        self.assertEqual(len(unlinked), 0)
        self.assertEqual(len(missing), 0)

    def test_broken_image_in_ignored_file_is_suppressed(self):
        """
        Missing images in ignored markdown files should not be reported in missing_images.
        """
        ignored_sub = os.path.join(self.content_dir, 'ignored_section')
        os.makedirs(ignored_sub)
        with open(os.path.join(self.content_dir, '.lintignore'), 'w') as f:
            f.write('ignored_section/\n')

        with open(os.path.join(ignored_sub, 'page.md'), 'w', encoding='utf-8') as f:
            f.write('![Nonexistent](missing-image.png)\n')

        missing, _ = validate_missing(self.content_dir, self.test_dir, content_dir=self.content_dir)
        self.assertEqual(len(missing), 0)

    def test_broken_image_in_unignored_file_is_reported(self):
        """
        Missing images in active (non-ignored) markdown files must be flagged.
        """
        valid_dir = os.path.join(self.content_dir, 'active_section')
        os.makedirs(valid_dir)
        with open(os.path.join(valid_dir, 'page.md'), 'w', encoding='utf-8') as f:
            f.write('![Nonexistent](missing-image.png)\n')

        missing, _ = validate_missing(self.content_dir, self.test_dir, content_dir=self.content_dir)
        self.assertEqual(len(missing), 1)

    def test_genuinely_unlinked_asset_is_detected(self):
        """
        Assets never referenced by ANY markdown file must still be flagged as unlinked.
        """
        assets_dir = os.path.join(self.content_dir, 'assets')
        os.makedirs(assets_dir)
        orphan_path = os.path.join(assets_dir, 'orphan.png')
        with open(orphan_path, 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n')

        _, referenced = validate_missing(self.content_dir, self.test_dir, content_dir=self.content_dir)
        assets = get_all_assets(self.content_dir, self.test_dir)
        unlinked = assets - referenced
        self.assertEqual(unlinked, {os.path.normpath(orphan_path)})

    def test_remove_unlinked_cli_deletes_orphan_and_preserves_ignored_doc_reference(self):
        """
        Review item 1: Entry-point test asserting that remove-unlinked deletes a genuine orphan
        while preserving an image referenced by an ignored document.
        """
        assets_dir = os.path.join(self.content_dir, 'shared', 'assets')
        os.makedirs(assets_dir)
        kept_img = os.path.join(assets_dir, 'kept.png')
        orphan_img = os.path.join(assets_dir, 'review-orphan.png')
        with open(kept_img, 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n')
        with open(orphan_img, 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n')

        # Create ignored document referencing kept_img
        ignored_sub = os.path.join(self.content_dir, 'software', 'app-lab', 'cli')
        os.makedirs(ignored_sub)
        with open(os.path.join(self.content_dir, 'software', 'app-lab', '.lintignore'), 'w') as f:
            f.write('cli/\n')

        md_file = os.path.join(ignored_sub, 'guide.md')
        rel_img = os.path.relpath(kept_img, ignored_sub).replace('\\', '/')
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(f'# App Lab CLI\n\n![Screenshot]({rel_img})\n')

        # Before removal, validate-unlinked CLI detects the orphan and exits with 1
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as cm:
                image_links_main(["validate-unlinked", self.content_dir])
            self.assertEqual(cm.exception.code, 1)

        # Run remove-unlinked CLI entry point
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(io.StringIO()):
            image_links_main(["remove-unlinked", self.content_dir])

        # Assert genuine orphan was deleted, and referenced image was preserved
        self.assertFalse(os.path.exists(orphan_img), "Genuine orphan image was not deleted by remove-unlinked")
        self.assertTrue(os.path.exists(kept_img), "Image referenced by ignored doc was wrongly deleted")
        self.assertIn("review-orphan.png", stdout.getvalue())

        # Validate-unlinked CLI now passes cleanly
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            # Returns normally without raising SystemExit(1)
            image_links_main(["validate-unlinked", self.content_dir])


class TestRelativeLinksIgnoreDecoupling(unittest.TestCase):
    def setUp(self):
        REL_IGNORE_CACHE.clear()
        self.test_dir = tempfile.mkdtemp()
        self.content_dir = os.path.join(self.test_dir, 'content')
        os.makedirs(self.content_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        REL_IGNORE_CACHE.clear()

    def test_build_route_map_indexes_ignored_files(self):
        """
        Tests the extracted route-indexing function build_route_map() directly to ensure
        files in ignored directories are present in the route map.
        """
        legacy_dir = os.path.join(self.content_dir, 'hardware', 'legacy-mkr')
        os.makedirs(legacy_dir)
        with open(os.path.join(self.content_dir, '.lintignore'), 'w') as f:
            f.write('hardware/legacy-mkr\n')

        legacy_file = os.path.join(legacy_dir, 'mkr-zero.md')
        with open(legacy_file, 'w', encoding='utf-8') as f:
            f.write('# MKR Zero\n')

        routes = build_route_map(self.content_dir)
        expected_url = map_file_to_url(legacy_file, self.content_dir)
        self.assertIn(expected_url, routes)
        self.assertIn(legacy_file, routes[expected_url])

    def test_main_validate_active_linking_to_ignored_target_and_anchor(self):
        """
        Review item 2: Production discovery and validation exercised through main().
        - Active page links to an ignored target and an anchor within it.
        - Broken outbound links in the ignored page remain suppressed.
        - Validation completes cleanly.
        """
        # Create ignored legacy hardware section with an anchor AND a broken outbound link
        legacy_dir = os.path.join(self.content_dir, 'hardware', 'legacy-mkr')
        os.makedirs(legacy_dir)
        with open(os.path.join(self.content_dir, '.lintignore'), 'w') as f:
            f.write('hardware/legacy-mkr\n')

        legacy_file = os.path.join(legacy_dir, 'mkr-zero.md')
        with open(legacy_file, 'w', encoding='utf-8') as f:
            f.write(
                '# MKR Zero\n\n'
                '## Pinout\n'
                'Pinout details here.\n\n'
                'Check out [Broken Outbound Link](/does/not/exist/) and '
                '[Broken Outbound Anchor](/also/missing/#anchor).\n'
            )

        # Create active unignored section linking to the legacy section and its anchor
        active_dir = os.path.join(self.content_dir, 'software', 'app-lab')
        os.makedirs(active_dir)
        active_file = os.path.join(active_dir, 'getting-started.md')
        with open(active_file, 'w', encoding='utf-8') as f:
            f.write(
                '# Getting Started\n\n'
                'Check out [MKR Zero](/hardware/legacy-mkr/) and '
                '[MKR Zero Pinout](/hardware/legacy-mkr/#pinout) for hardware details.\n'
            )

        # Run production discovery and validation through relative_links main()
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(io.StringIO()):
            # Must complete without SystemExit(1)
            relative_links_main(["validate", self.content_dir])

        self.assertIn("Validation successful", stdout.getvalue())

    def test_main_validate_broken_link_to_nonexistent_page_fails(self):
        """
        Review item 2: Genuine missing targets still fail in production main() validation.
        """
        active_dir = os.path.join(self.content_dir, 'software')
        os.makedirs(active_dir)
        active_file = os.path.join(active_dir, 'intro.md')
        with open(active_file, 'w', encoding='utf-8') as f:
            f.write('# Intro\n\n[Broken Link](/does/not/exist/)\n')

        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as cm:
                relative_links_main(["validate", self.content_dir])
            self.assertEqual(cm.exception.code, 1)

        self.assertIn("Broken link", stdout.getvalue())
        self.assertIn("/does/not/exist/", stdout.getvalue())

    def test_main_validate_broken_anchor_fails(self):
        """
        Review item 2: Genuine missing anchors in valid/ignored targets still fail in production main().
        """
        legacy_dir = os.path.join(self.content_dir, 'hardware', 'legacy-mkr')
        os.makedirs(legacy_dir)
        with open(os.path.join(self.content_dir, '.lintignore'), 'w') as f:
            f.write('hardware/legacy-mkr\n')

        with open(os.path.join(legacy_dir, 'mkr-zero.md'), 'w', encoding='utf-8') as f:
            f.write('# MKR Zero\n\n## Valid Anchor\nContent.\n')

        active_dir = os.path.join(self.content_dir, 'software')
        os.makedirs(active_dir)
        with open(os.path.join(active_dir, 'guide.md'), 'w', encoding='utf-8') as f:
            f.write('# Guide\n\n[Broken Anchor](/hardware/legacy-mkr/#missing-anchor)\n')

        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as cm:
                relative_links_main(["validate", self.content_dir])
            self.assertEqual(cm.exception.code, 1)

        self.assertIn("Broken anchor", stdout.getvalue())
        self.assertIn("#missing-anchor", stdout.getvalue())

    def test_multi_file_route_anchor_validation(self):
        """
        Pages comprised of multiple markdown files (overview.md, tech-specs.md, etc.)
        should allow anchors defined in any of the contributing files.
        """
        board_dir = os.path.join(self.content_dir, 'hardware', 'uno-q')
        os.makedirs(board_dir)

        # File 1: overview
        with open(os.path.join(board_dir, 'overview.md'), 'w', encoding='utf-8') as f:
            f.write('# Overview\n\n## Pinout\nPinout details here.\n')

        # File 2: tech-specs
        with open(os.path.join(board_dir, 'tech-specs.md'), 'w', encoding='utf-8') as f:
            f.write('# Tech Specs\n\n## Power Ratings\nPower details.\n')

        # File 3: active tutorial linking to #pinout
        tut_dir = os.path.join(self.content_dir, 'tutorials')
        os.makedirs(tut_dir)
        tut_file = os.path.join(tut_dir, 'guide.md')
        with open(tut_file, 'w', encoding='utf-8') as f:
            f.write('# Guide\n\nSee [Uno Q Pinout](/hardware/uno-q/#pinout).\n')

        valid_production_paths = build_route_map(self.content_dir)
        anchor_cache = {}
        issues = validate_file(tut_file, valid_production_paths, self.content_dir, anchor_cache)
        self.assertEqual(issues, [])


if __name__ == '__main__':
    unittest.main()
