define(['js/discovery/collections/filters'], function(Filters) {
    'use strict';

    describe('discovery.collections.Filters', function () {

        beforeEach(function () {
            this.filters = new Filters([
                { type: 'org', query: 'edX', name: 'edX'},
                { type: 'language', query: 'English', name: 'English'}
            ]);
        });

        it('converts to a dictionary', function () {
            expect(this.filters.getTerms()).toEqual({
                org: 'edX',
                language: 'English'
            });
        });

    });

});
